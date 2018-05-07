#This script creates a postgres database hosted in docker container and uploads data from
#a kaggle csv dataset to populate the database
#data acquired from: https://www.kaggle.com/drgilermo/nba-players-stats/version/1
####################################################################################
import os
from sqlalchemy import create_engine
import pandas as pd


#local variables stored in the os env
user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'db'
port = '5432'
engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db))
conn = engine.connect()

#runs once to intialize the database
def table_initialization(columns):
    conn.execute('''CREATE TABLE "NBA Stats" ("Index" varchar(50) NOT NULL, PRIMARY KEY ("Index"));''')
    for column in columns:
        if column != 'Index':
            conn.execute('''ALTER TABLE "NBA Stats" ADD COLUMN "{}" VARCHAR(50);'''.format(str(column)))

#runs to transfer data from csv to postgres DB
def data_insertion(df):
    #keeps track of progress
    counter = 0
    for index, row in df.iterrows():
        #Inserts ach row or data from csv into sql statement and uploads to database
        #the apostrophe in name like Shaq O'Neal needs to be handled
        if "'" in str(row['Player']):
            player = str(row['Player']).replace("'", '')
            conn.execute('''INSERT INTO "NBA Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], player, row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
        else:
            conn.execute('''INSERT INTO "NBA Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
        counter += 1
        #Prints out occasional progress report
        if counter % 2000 == 0:
            print(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS'])


def init_db():
    # Builds the database with init_db() on docker-compose build and initializes
    #the db fields for the canary api
    #gets data from csv
    df = pd.read_csv(open('Seasons_Stats.csv'))
    columns = df.columns.values
    #runs once to intialize the database
    table_initialization(columns)
    #runs to transfer data from csv to postgres DB
    data_insertion(df)
