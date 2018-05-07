from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
#Don't want to deal with CSRF
from django.views.decorators.csrf import csrf_exempt
#El classico
import json
from sqlalchemy import create_engine
#fancy dictionary sorting
from operator import itemgetter
#for handling nan types in data
from numpy import nansum
from pandas import isnull

#connects to my database
engine = create_engine('postgres://iwogouitiuowon:a1e97051f3c10aff7a0d0fedcaf759a7b259be0130e4a6b1790ed5c6c70a02e1@ec2-54-221-220-59.compute-1.amazonaws.com:5432/daepj190brg9i7')#10 million rows
conn = engine.connect()

available_columns_to_use = ['Index', 'Year', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'PER', 'TSPercent', '3PAr', 'FTr', 'ORBPercent', 'DRBPercent', 'TRBPercent', 'ASTPercent', 'STLPercent', 'BLKPercent', 'TOVPercent', 'USGPercent', 'blanl', 'OWS', 'DWS', 'WS', 'WS/48', 'blank2', 'OBPM', 'DBPM', 'BPM', 'VORP', 'FG', 'FGA', 'FGPercent', '3P', '3PA', '3PPercent', '2P', '2PA', '2PPercent', 'eFGPercent', 'FT', 'FTA', 'FTPercent', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

# My views are here.
@csrf_exempt #As this is an unpaid proejct I'm skipping CSRF Protocal
def index(request):
    return render(request, 'Homepage.html')

#APIs

#Get all column names
@csrf_exempt
def all_column_names(request):
    all_column_names_raw = conn.execute('''SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{}';'''.format('NBA Stats'))
    all_column_names = all_column_names_raw.cursor.fetchall()
    acn = [i[3] for i in all_column_names]
    return JsonResponse(acn, safe=False)

#Gets all of a players records for a specific category over the course of their career
@csrf_exempt
def category_over_player_career(request):
    data = json.loads(request.body.decode('utf-8'))
    category = data["category"]
    player = data["player"]

    first_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Player" = '{}';'''.format(category, player))
    first_column_query = first_column_query_raw.cursor.fetchall()
    #gets a list of all years they played
    year_query_raw = conn.execute('''SELECT "Year" FROM "NBA Stats" WHERE "Player" = '{}';'''.format(player))
    year_query = year_query_raw.cursor.fetchall()

    #Builds th data object to send
    list_of_dictionarys_to_send = []
    counter = 0
    for annual_point_stat in first_column_query:
        year = int(str(year_query[counter][0])[:-2])#All the years end in .0 as in 2016.0
        list_of_dictionarys_to_send.append({category:annual_point_stat[0], "Year":year})
        counter += 1

    return JsonResponse(list_of_dictionarys_to_send, safe=False)

#Graph any category for a team since and choose which years
@csrf_exempt
def category_over_team_existence(request):
    #Gets all of a players records for a specific category over the course of their career
    data = json.loads(request.body.decode('utf-8'))
    category = data["category"]
    team = data["team"]

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

    return JsonResponse(list_of_dictionarys_to_send, safe=False)

#//Graph top 20 players for any category in any year
@csrf_exempt
def top_20_players_in_category_for_year(request):
    data = json.loads(request.body.decode('utf-8'))
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

    return JsonResponse(finalList, safe=False)

#get all players
@csrf_exempt
def get_individual_column(request):
    data = json.loads(request.body.decode('utf-8'))
    Column_Name = data["columnName"]
    column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats";'''.format(Column_Name))
    column_query = column_query_raw.cursor.fetchall()
    if Column_Name == "Player":
        col_query_filtered = []
        for i in column_query:
            if i[0] not in col_query_filtered:
                col_query_filtered.append(i[0])
        return JsonResponse(col_query_filtered, safe=False)
    else:
        col_query_filtered = [i[0] for i in column_query]
        return JsonResponse(col_query_filtered, safe=False)

#get all players from 2016
@csrf_exempt
def one_paramter_query(request):
    data = json.loads(request.body.decode('utf-8'))

    Column_Name = data["columnName"] #"Player"
    specfied_condition = data["specfiedCondition"] #"Year"
    specfied_condition_parameter = data["specfiedConditionParameter"] #"2016.0"

    one_paramter_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "{}" = '{}';'''.format(Column_Name, specfied_condition, specfied_condition_parameter))
    one_paramter_query = one_paramter_query_raw.cursor.fetchall()

    list_of_dictionarys_to_send = []

    for i in one_paramter_query:
        temp_dict = {}
        temp_dict[Column_Name] = i[0]
        list_of_dictionarys_to_send.append(temp_dict)

    return JsonResponse(list_of_dictionarys_to_send, safe=False)

#get all stats for tony snell in all years he played
@csrf_exempt
def two_parameter_query(request):
    data = json.loads(request.body.decode('utf-8'))

    Column_Name = data["columnName"] #"Player"
    specfied_condition = data["columnParamerter"] #"Tony Snell"

    two_parameter_query_raw = conn.execute('''SELECT * FROM "NBA Stats" WHERE "{}" = '{}';'''.format(Column_Name, specfied_condition))
    two_parameter_query = two_parameter_query_raw.cursor.fetchall()

    list_of_dictionarys_to_send = []

    for data_tuple in two_parameter_query:
        data_column_dictionary = {}
        counter = 0
        for data_points in data_tuple:
            current_column = available_columns_to_use[counter]
            data_column_dictionary[current_column] = data_points
            counter += 1
        list_of_dictionarys_to_send.append(data_column_dictionary)

    return JsonResponse(list_of_dictionarys_to_send, safe=False)

#get all stats for tony snell in a specific year: 2016.0
@csrf_exempt
def three_parameter_query(request):
    data = json.loads(request.body.decode('utf-8'))

    Column_Name = data["columnName"] #"Player"
    Column_Paramerter_One = data["columnParamerterOne"] #"Tony Snell"
    Second_Column_Name = data["secondColumnName"] #"Year"
    Column_Paramerter_Two = data["columnParamerterTwo"] #"2016.0"

    three_parameter_query_raw = conn.execute('''SELECT * FROM "NBA Stats" WHERE "{}" = '{}' AND "{}" = '{}';'''.format(Column_Name, Column_Paramerter_One, Second_Column_Name, Column_Paramerter_Two))
    three_parameter_query = three_parameter_query_raw.cursor.fetchall()

    list_of_dictionarys_to_send = []

    for data_tuple in three_parameter_query:
        data_column_dictionary = {}
        counter = 0
        for data_points in data_tuple:
            current_column = available_columns_to_use[counter]
            data_column_dictionary[current_column] = data_points
            counter += 1
        list_of_dictionarys_to_send.append(data_column_dictionary)

    return JsonResponse(list_of_dictionarys_to_send, safe=False)
