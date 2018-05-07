#This program creates a postgres database hosted on heroku and uploads data from
#a kaggle csv dataset to populate the database
#data acquired from: https://www.kaggle.com/drgilermo/nba-players-stats/version/1
####################################################################################
import pandas as pd
from sqlalchemy import create_engine

#connects to my database
engine = create_engine('postgres://iwogouitiuowon:a1e97051f3c10aff7a0d0fedcaf759a7b259be0130e4a6b1790ed5c6c70a02e1@ec2-54-221-220-59.compute-1.amazonaws.com:5432/daepj190brg9i7')#10 million rows
conn = engine.connect()

#gets data from csv
df = pd.read_csv(open('Seasons_Stats.csv'))
columns = df.columns.values

#runs once to intialize the database
def table_initialization():
    conn.execute('''CREATE TABLE "NBA Stats" ("Index" varchar(50) NOT NULL, PRIMARY KEY ("Index"));''')
    for column in columns:
        print(column)
        if column != 'Index':
            conn.execute('''ALTER TABLE "NBA Stats" ADD COLUMN "{}" VARCHAR(50);'''.format(str(column)))
table_initialization()

#runs to transfer data from csv to postgres DB
def data_insertion():
    #keeps track of progress
    counter = 0
    for index, row in df.iterrows():
        #Inserts ach row or data from csv into sql statement and uploads to database
        conn.execute('''INSERT INTO "NBA Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
        counter += 1
        #Prints out occasional progress report
        if counter % 200 == 0:
            print(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS'])
data_insertion()
