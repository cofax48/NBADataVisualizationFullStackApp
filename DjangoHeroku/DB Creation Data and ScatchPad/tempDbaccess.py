###This was a scratchpad that I used to build my apis so that I wouldn't have to
# restart the sever every time I wanted to change something in the view

from sqlalchemy import create_engine
from django.http import JsonResponse
from operator import itemgetter
from numpy import nansum
from pandas import isnull

#connects to my database
engine = create_engine('postgres://iwogouitiuowon:a1e97051f3c10aff7a0d0fedcaf759a7b259be0130e4a6b1790ed5c6c70a02e1@ec2-54-221-220-59.compute-1.amazonaws.com:5432/daepj190brg9i7')#10 million rows
conn = engine.connect()

Column_Name = "Tm"
category = "PTS"
team = "NJN"
player = "Carmelo Anthony"
specfied_condition = "Year"
specfied_condition_parameter = "1953.0"
year = "2016.0"
available_columns_to_use = ['Index', 'Year', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'PER', 'TSPercent', '3PAr', 'FTr', 'ORBPercent', 'DRBPercent', 'TRBPercent', 'ASTPercent', 'STLPercent', 'BLKPercent', 'TOVPercent', 'USGPercent', 'blanl', 'OWS', 'DWS', 'WS', 'WS/48', 'blank2', 'OBPM', 'DBPM', 'BPM', 'VORP', 'FG', 'FGA', 'FGPercent', '3P', '3PA', '3PPercent', '2P', '2PA', '2PPercent', 'eFGPercent', 'FT', 'FTA', 'FTPercent', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

def category_over_player_career():
    #Gets all of a players records for a specific category over the course of their career
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

    print(list_of_dictionarys_to_send)
#category_over_player_career()

#Graph any category for a team since and choose which years
def category_over_team_existence():
    #Gets all of a players records for a specific category over the course of their career
    first_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Tm" = '{}';'''.format(category, team))
    first_column_query = first_column_query_raw.cursor.fetchall()
    #gets a list of all years they played
    year_query_raw = conn.execute('''SELECT "Year" FROM "NBA Stats" WHERE "Tm" = '{}';'''.format(team))
    year_query = year_query_raw.cursor.fetchall()
    print(first_column_query)
    print(year_query)

    #Builds th data object to send
    list_of_dictionarys_to_send = []
    counter = 0
    current_year = 0
    combined_team_stat_for_category = 0
    temp_aggregate_of_player_stats_for_season = []

    if category == "PTS":
        gs_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Tm" = '{}';'''.format("G", team))
        gs_column_query = gs_column_query_raw.cursor.fetchall()
        #cycles through all player stats from team for year
        yearly_pt_totals = []
        game_counter = 0
        for individuals_annual_point_stat_on_team in first_column_query:
            year = int(str(year_query[counter][0])[:-2])#All the years end in .0 as in 2016.0
            if current_year == year:
                print(year)
                print(individuals_annual_point_stat_on_team[0])
                print(gs_column_query[game_counter][0])
                averaged_points_per_game = float(individuals_annual_point_stat_on_team[0]) / float(gs_column_query[game_counter][0])
                print(averaged_points_per_game)
                print(yearly_pt_totals)
                yearly_pt_totals.append(averaged_points_per_game)
                game_counter += 1
                counter += 1
                """
                #print(season_point_totals)
                #print(gs_column_query[game_counter])
                #print(gs_column_query[game_counter][0])
                games_played_per_season = gs_column_query[game_counter][0]
                averaged_points_per_game = float(individuals_annual_point_stat_on_team[0]) / float(games_played_per_season)
                print(averaged_points_per_game)
                yearly_pt_totals.append(averaged_points_per_game)
                game_counter += 1

                print(yearly_pt_totals)


                current_year = year
                #list_of_dictionarys_to_send.append({category:annual_point_stat[0], "Year":year})
                counter += 1
                #print(averaged_stats)
                list_of_dictionarys_to_send.append({category:sum(yearly_pt_totals), "Year":year})
                """
            else:
                print(current_year)
                print(yearly_pt_totals)
                print(sum(yearly_pt_totals))
                list_of_dictionarys_to_send.append({category:sum(yearly_pt_totals), "Year":current_year})
                yearly_pt_totals = []
            current_year = year
            #list_of_dictionarys_to_send.append({category:annual_point_stat[0], "Year":year})
            #counter += 1
    else:
        #cycles through all player stats from team for year
        for individuals_annual_point_stat_on_team in first_column_query:
            year = int(str(year_query[counter][0])[:-2])#All the years end in .0 as in 2016.0
            #checks to avoid duplication of years
            if current_year == year:
                temp_aggregate_of_player_stats_for_season.append(float(individuals_annual_point_stat_on_team[0]))
            else:
                if len(temp_aggregate_of_player_stats_for_season) != 0:
                    #print(year)
                    print(temp_aggregate_of_player_stats_for_season)

                    #Factoring for number of missing data Fields and averaging the
                    #raw score using Numpy and and Pandas and Numpy nan type handling
                    number_of_nan = int(sum([isnull(i) for i in temp_aggregate_of_player_stats_for_season]))
                    print(year)
                    print(number_of_nan)
                    real_len = int(len(temp_aggregate_of_player_stats_for_season))
                    print(real_len)
                    dvisible_number = int(real_len - number_of_nan)
                    num_sum = nansum(temp_aggregate_of_player_stats_for_season[1::2])
                    print(num_sum)
                    averaged_stats = num_sum / dvisible_number
                    if isnull(averaged_stats) == False:
                        print(averaged_stats)
                        list_of_dictionarys_to_send.append({category:averaged_stats, "Year":year})

                    """
                    #averages the stats from the number of team players
                    summed_stats = sum(temp_aggregate_of_player_stats_for_season)
                    averaged_stats = summed_stats / len(temp_aggregate_of_player_stats_for_season)
                    #print(averaged_stats)
                    list_of_dictionarys_to_send.append({category:averaged_stats, "Year":year})
                    #print({category:combined_team_stat_for_category, "Year":current_year})
                    temp_aggregate_of_player_stats_for_season = []
                    """
            current_year = year
            #list_of_dictionarys_to_send.append({category:annual_point_stat[0], "Year":year})
            counter += 1

    print(list_of_dictionarys_to_send)

category_over_team_existence()

#//Graph top players for any category in any year
def top_20_players_in_category_for_year():
    two_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "Year" = '{}';'''.format(category, year))
    two_column_query = two_column_query_raw.cursor.fetchall()
    player_query_raw = conn.execute('''SELECT "Player" FROM "NBA Stats" WHERE "Year" = '{}';'''.format(year))
    player_query = player_query_raw.cursor.fetchall()

    list_of_dictionarys_to_send_temp = []

    counter = 0
    highest_20_stats_from_category = []
    current_player = '' #players who played on more than one team in a season have thir stats split
    for stat in two_column_query:
        player = player_query[counter][0]
        stat = stat[0]
        list_of_dictionarys_to_send_temp.append({"Player":player, category:float(stat)})

        print(player, stat)
        counter += 1
    #print(two_column_query)
    #print(player_query)
    print(list_of_dictionarys_to_send_temp)
    newlist = sorted(list_of_dictionarys_to_send_temp, key=itemgetter(category))[-20:]
    print(len(newlist))
#top_20_players_in_category_for_year()

def all_column_names():
    all_column_names_raw = conn.execute('''SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{}';'''.format('NBA Stats'))
    all_column_names = all_column_names_raw.cursor.fetchall()
    acn = [i[3] for i in all_column_names]
    return JsonResponse(acn)

def all_data_from_specific_column():
    #gets all data from specific column
    column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats";'''.format(Column_Name))
    column_query = column_query_raw.cursor.fetchall()
    if Column_Name == "Player":
        col_query_filtered = []
        for i in column_query:
            if i[0] not in col_query_filtered:
                col_query_filtered.append(i[0])
        return JsonResponse(col_query_filtered, safe=False)
    else:
        col_query_filtered = []
        for i in column_query:
            if i[0] not in col_query_filtered:
                col_query_filtered.append(i[0])
        print(col_query_filtered)

#all_data_from_specific_column()

def all_data_from_specified_query():
    #gets all data from specified query
    two_column_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "{}" = '{}';'''.format(Column_Name, specfied_condition, specfied_condition_parameter))
    two_column_query = two_column_query_raw.cursor.fetchall()
    print(two_column_query)

def one_paramter_querys():
    one_paramter_query_raw = conn.execute('''SELECT "{}" FROM "NBA Stats" WHERE "{}" = '{}';'''.format(Column_Name, specfied_condition, specfied_condition_parameter))
    one_paramter_query = one_paramter_query_raw.cursor.fetchall()
    list_of_dictionarys_to_send = []


    for i in one_paramter_query:
        temp_dict = {}
        temp_dict[Column_Name] = i[0]
        list_of_dictionarys_to_send.append(temp_dict)
    print(list_of_dictionarys_to_send)

    #return JsonResponse(list_of_dictionarys_to_send, safe=False)
#one_paramter_querys()

def two_parameter_querys():
    Column_Name = "Player"
    specfied_condition = "Tony Snell"
    two_parameter_query_raw = conn.execute('''SELECT * FROM "NBA Stats" WHERE "{}" = '{}';'''.format(Column_Name, specfied_condition))
    two_parameter_query = two_parameter_query_raw.cursor.fetchall()
    list_of_dictionarys_to_send = []

    print(two_parameter_query)
    for data_tuple in two_parameter_query:
        print(data_tuple)
        data_column_dictionary = {}
        counter = 0
        for data_points in data_tuple:
            print(data_points)
            current_column = available_columns_to_use[counter]
            print(current_column)
            data_column_dictionary[current_column] = data_points
            counter += 1
        list_of_dictionarys_to_send.append(data_column_dictionary)

    print(list_of_dictionarys_to_send)

#two_parameter_querys()

def three_parameter_query():
    two_column_query_raw = conn.execute('''SELECT * FROM "NBA Stats" WHERE "Player" = 'Tony Snell' AND "Year" = '2016.0';'''.format(Column_Name))
    two_column_query = two_column_query_raw.cursor.fetchall()
    print(two_column_query)
#three_parameter_query()



#print(column_query)
#print(two_column_query)

#I want to get data for each category

#each category by year
#each category by team
