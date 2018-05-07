#Flask app: serve apis, gets data from my db and connect my homepage
import datetime
import os
#El Classico
from flask import Flask, abort
from flask import request, render_template
from flask import jsonify
from flask import Response
from sqlalchemy import create_engine
#fancy dictionary sorting
from operator import itemgetter
#Self explanatory
import json
from datetime import datetime
import time
#for handling nan types in data
from numpy import nansum
from pandas import isnull
#Gets db params
from database import engine

#intializes app and connects to my database
app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']
conn = engine.connect()

#Homepage
@app.route("/", methods=['GET'])
def index():
    return render_template('Homepage.html')

#APIs
#Gets all of a players records for a specific category over the course of their career
@app.route("/category_over_player_career", methods=['POST'])
def category_over_player_career():
    if request.method == 'POST':
        data = json.loads(request.data.decode())

        fields = [i for i in data]
        expected_fields = ["category", "player"]
        #If the expected data params equal the approved data params for this api then we proceeed
        if expected_fields == fields:
            category = data["category"]
            player = data["player"]

            #Gets all data from a category over a player's career -eg Steph Curry -3 point attempts
            first_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Player" = '{}';'''.format(category, player))
            first_column_query = first_column_query_raw.cursor.fetchall()
            #gets a list of all years they played
            year_query_raw = conn.execute('''SELECT "Year" FROM "NBA Stats" WHERE "Player" = '{}';'''.format(player))
            year_query = year_query_raw.cursor.fetchall()

            #Builds the data object to send
            list_of_dictionarys_to_send = []
            counter = 0
            for annual_point_stat in first_column_query:
                year = int(str(year_query[counter][0])[:-2])#All the years end in .0 as in 2016.0
                list_of_dictionarys_to_send.append({category:annual_point_stat[0], "Year":year})
                counter += 1

            return jsonify(list_of_dictionarys_to_send)
        else:
            #if the data is formatted for the api right then this is sent
            return abort(400)
    #returns if request is not "post"
    return abort(405)

@app.route("/category_over_team_existence", methods=['POST'])
def category_over_team_existence():
    #Gets all of a players records for a specific category over the course of their career
    if request.method == 'POST':
        data = json.loads(request.data.decode())

        fields = [i for i in data]
        expected_fields = ["category", "team"]
        #If the expected data params equal the approved data params for this api then we proceeed
        if expected_fields == fields:
            category = data["category"]
            team = data["team"]

            #Gets all data from a category over a team's existence -eg Knicks -3 point attempts
            first_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Tm" = '{}';'''.format(category, team))
            first_column_query = first_column_query_raw.cursor.fetchall()
            #gets a list of all years the team was in existence
            year_query_raw = conn.execute('''SELECT "Year" FROM "NBA Stats" WHERE "Tm" = '{}';'''.format(team))
            year_query = year_query_raw.cursor.fetchall()

            #Builds th data object to send
            list_of_dictionarys_to_send = []
            counter = 0
            current_year = 0
            combined_team_stat_for_category = 0
            temp_aggregate_of_player_stats_for_season = []
            #cycles through all player stats from team for year
            for individuals_annual_point_stat_on_team in first_column_query:
                year = int(str(year_query[counter][0])[:-2])#All the years end in .0 as in 2016.0
                #checks to avoid duplication of years
                if current_year == year:
                    temp_aggregate_of_player_stats_for_season.append(float(individuals_annual_point_stat_on_team[0]))
                else:
                    #averages the stats from the number of team players
                    if len(temp_aggregate_of_player_stats_for_season) != 0:
                        #Factoring for number of missing data Fields and averaging the
                        #raw score using Numpy and and Pandas and Numpy nan type handling
                        number_of_nan = int(sum([isnull(i) for i in temp_aggregate_of_player_stats_for_season]))
                        real_len = int(len(temp_aggregate_of_player_stats_for_season))
                        dvisible_number = int(real_len - number_of_nan)
                        num_sum = nansum(temp_aggregate_of_player_stats_for_season[1::2])
                        averaged_stats = num_sum / dvisible_number
                        if isnull(averaged_stats) == False:
                            list_of_dictionarys_to_send.append({category:averaged_stats, "Year":year})

                #housekeeping
                current_year = year
                counter += 1

            return jsonify(list_of_dictionarys_to_send)
        else:
            return abort(400)
    return abort(405)

#Graph top 20 players for any category in any year
@app.route("/top_20_players_in_category_for_year", methods=['POST'])
def top_20_players_in_category_for_year():
    if request.method == 'POST':
        data = json.loads(request.data.decode())

        fields = [i for i in data]
        expected_fields = ["category", "year"]
        #If the expected data params equal the approved data params for this api then we proceeed
        if expected_fields == fields:
            category = data["category"]
            year = data["year"]
            year = str(year) + ".0"#All the years end in .0

            two_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Year" = '{}';'''.format(category, year))
            two_column_query = two_column_query_raw.cursor.fetchall()
            player_query_raw = conn.execute('''SELECT "Player" FROM "NBA Stats" WHERE "Year" = '{}';'''.format(year))
            player_query = player_query_raw.cursor.fetchall()

            list_of_dictionarys_to_send_temp = []

            counter = 0
            #filters through th results to create a dictionary
            for stat in two_column_query:
                player = player_query[counter][0]
                stat = stat[0]
                list_of_dictionarys_to_send_temp.append({"Player":player, category:float(stat)})

                counter += 1

            #sorts the list of dicts by value and keeps only the top 20 in category
            finalList = sorted(list_of_dictionarys_to_send_temp, key=itemgetter(category))[-21:]

            return jsonify(finalList)
        else:
            return abort(400)
    return abort(405)

#get all players-really only used to just populate the list of available players from which the user can select
@app.route("/get_individual_column", methods=['POST'])
def get_individual_column():
    #I use POST since anytime I get data from the database I'd rather wrap it in a post call
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        Column_Name = data["columnName"]
        column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats";'''.format(Column_Name))
        column_query = column_query_raw.cursor.fetchall()
        if Column_Name == "Player":
            col_query_filtered = []
            for i in column_query:
                if i[0] not in col_query_filtered:
                    col_query_filtered.append(i[0])
            return jsonify(col_query_filtered)
        else:
            col_query_filtered = [i[0] for i in column_query]
            return jsonify(col_query_filtered)
    return abort(405)

#Gets the party started
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
