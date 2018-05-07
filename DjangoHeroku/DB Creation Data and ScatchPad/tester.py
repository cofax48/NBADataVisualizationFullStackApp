###This was a scratchpad that I used to build any lists needed for the project
#so I wouldn't have to write them by hand

def year_maker():
    year_list = []
    for i in range(1950, 2018):
        year_list.append(str(i))

    print(year_list)

cat_list = ['Year', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'PER', 'TSPercent', '3PAr', 'ORBPercent', 'DRBPercent', 'TRBPercent', 'ASTPercent', 'STLPercent', 'BLKPercent', 'TOVPercent', 'USGPercent', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP',
'FG', 'FGA', 'FGPercent', '3P', '3PA', '3PPercent', '2P', '2PA', '2PPercent', 'eFGPercent', 'FT', 'FTA', 'FTPercent', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'];
cats = """Age -- Age of Player at the start of February 1st of that season.
Tm -- Team
Lg -- League
Pos -- Position
G -- Games
GS -- Games Started
MP -- Minutes Played Per Game
FG -- Field Goals Per Game
FGA -- Field Goal Attempts Per Game
FG% -- Field Goal Percentage
3P -- 3-Point Field Goals Per Game
3PA -- 3-Point Field Goal Attempts Per Game
3P% -- 3-Point Field Goal Percentage
2P -- 2-Point Field Goals Per Game
2PA -- 2-Point Field Goal Attempts Per Game
2P% -- 2-Point Field Goal Percentage
eFG% -- Effective Field Goal Percentage
FT -- Free Throws Per Game
FTA -- Free Throw Attempts Per Game
FT% -- Free Throw Percentage
ORB -- Offensive Rebounds Per Game
DRB -- Defensive Rebounds Per Game
TRB -- Total Rebounds Per Game
AST -- Assists Per Game
STL -- Steals Per Game
BLK -- Blocks Per Game
TOV -- Turnovers Per Game
PF -- Personal Fouls Per Game
PTS -- Points Per Game
PER -- Player Efficency Rating
TSPercent -- True Shooting Percentage
3PAr -- 3-Point Attempt Rate
ORBPercent -- Offensive Rebounds Per Game
DRBPercent -- Defensive Rebound Percentage
TRBPercent -- Total Rebound Percentage
ASTPercent -- Assist Percentage
STLPercent -- Steal Percentage
BLKPercent -- Block Percentage
TOVPercent -- Turnovers Percentage
USGPercent -- Usage Percentage
OBPM -- Offensive Box Plus/Minus
DBPM -- Defensive Box Plus/Minus
BPM -- Box Plus/Minus
OWS -- Offensive Win Shares
DWS -- Defensive Win Shares
WS -- Win Shares
WS/48 -- Win Shares Per 48 Minutes
VORP -- Value Over Replacement Player"""

list_of_dicts = []
abbrev_list = []
temp_list = []
fulln_list = []
for i in cats:
    temp_list.append(i)
    if i == '-':
        abbrev = ''.join(temp_list)
        if len(abbrev) > 1:
            abbrev_list.append(abbrev)
        temp_list = []
    if i == '\n':
        fulln = ''.join(temp_list)
        if len(fulln) > 1:
            abbre = str(abbrev_list[0]).split(' ')[0]
            if '%' in abbre:
                abbre = abbre.replace('%', 'Percent')
                list_of_dicts.append({"CatAbbrev":abbre, "FullCatName":fulln})
            else:
                list_of_dicts.append({"CatAbbrev":str(abbrev_list[0]).split(' ')[0], "FullCatName":fulln[:-1]})
                #fulln_list.append(fulln)
        temp_list = []
        abbrev_list = []

print(list_of_dicts)

def all_teams():
    allTeams = "AKF - Akron Firestone Non-Skids (NBL) AKG - Akron Goodyear Wingfoots (NBL) ANA - Anaheim Amigos (ABA) AND - Anderson Duffey Packers/Anderson Packers (NBL/NBA/NPBL) ATC - Atlanta Crackers (PBLA) ATG - Atlanta Glory (ABL) ATL - Atlanta Hawks (NBA) BAC - Baltimore Claws (ABA) BAL - Baltimore Bullets (NBA) BFB - Buffalo Bisons (NBL) BFG - Buffalo Germans (ABL) BIR - Birmingham Skyhawks (PBLA) BKA - Brooklyn Arcadians (ABL) BKC - Brooklyn Celtics (ABL) BKV - Brooklyn Visitations (ABL) BLB - Baltimore Bullets (ABL/BAA/NBA) BOS - Boston Celtics (BAA/NBA) BSW - Boston Whirlwinds (ABL) BTO - Baltimore Orioles (ABL) BUF - Buffalo Braves (NBA) CAD - California Dreams (WBL) CAP - Capital Bullets (NBA) CAR - Carolina Cougars (ABA) CCO - Chicago Condors (ABL) CHA - Charlotte Hornets (NBA) CHN - Charlotte Bobcats (NBA) CHB - Chicago Bruins (NBL) CHG - Chicago American Gears/Chicago Gears (NBL/PBLA) CHH - Chicago Hustle (WBL) CHI - Chicago Bulls (NBA) CHM - Chicago Majors (ABL) CHO - Chicago Bruins (ABL) CHP - Chicago Packers/Zephyrs (NBA) CHR - Charlotte Sting (WNBA) CHS - Chicago Stags (BAA/NBA) CHT - Chattanooga Majors (PBLA) CIN - Cincinnati Royals (NBA) CLA - Cleveland Allmen Transfers (NBL) CLC - Cleveland Chase Brass (NBL) CLE - Cleveland Cavaliers (NBA) CLP - Cleveland Pipers (ABL) CLR - Cleveland Rebels (BAA) CLW - Cleveland White Horses (NBL) COL - Coumbus Athletic Supply (NBL) COQ - Columbus Quest (ABL) COX - Colorado Explosion (ABL) CRK - Cleveland Rockers (WNBA) CRO - Cleveland Rosenblums (ABL) CSF - Chicago Studebaker Flyers (NBL) DAL - Dallas Mavericks (NBA) DEN - Denver Rockets/Nuggets (ABA/NBA) DET - Detroit Pistons (NBA) DLC - Dallas Chaparrals (NBA) DLD - Dallas Diamonds (WBL) DNV - Denver Nuggets (NBL/NBA/NPBL) DPP - Detroit Pulaski Post Five (ABL) DRO - Dayton Rockettes (WBL) DTC - Detroit Cardinals (ABL) DTE - Detroit Eagles (NBL) DTF - Detroit Falcons (BAA) DTG - Detroit Gems (NBL) DTL - Detroit Lions (ABL) DTS - Detroit Shock (WNBA) DTV - Detroit Vagabond Kings (NBL) DYM - Dayton Metros (NBL) DYR - Dayton Rens (NBL) ELP - East Liverpool Panthers (ABL) EVN - Evansville Agogans (NPBL) FLA - The Floridians (ABA) FTG - Fort Wayne General Electrics (NBL) FTW - Fort Wayne Zollner Pistons/Fort Wayne Pistons (NBL/BAA/NBA) FWC - Fort Wayne Caseys (ABL) FWH - Fort Wayne Hoosiers (ABL) GRH - Grand Rapids Hornets (NPBL) GRR - Grand Rapids Rangers (PBLA) GST - Golden State Warriors (NBA) HAW - Hawaii Chiefs (ABL) HCA - Hammond Ciesar All-Americans (NBL) HCB - Hammond Calumet Buccaneers (NBL) HOU - Houston Rockets (NBA) HSM - Houston Mavericks (PBLA) HST - Houston Mavericks (ABA) HTA - Houston Angels (WBL) HTC - Houston Comets (WNBA) IND - Indiana Pacers (ABA/NBA) INJ - Indianapolis Kautskys/Indianapolis Jets (NBL/BAA) INO - Indianapolis Olympians (NBA) IOW - Iowa Cornets (WBL) KAN - Kankakee Gallagher Trojans (NBL) KCB - Kansas City Blues (PBLA) KCH - Kansas City Hi-Spots (NPBL) KCK - Kansas City Kings (NBA) KCO - Kansas City-Omaha Kings (NBA) KCS - Kansas City Steers (ABL) KEN - Kentucky Colonels (ABA) LAC - Los Angeles Clippers (NBA) LAJ - Los Angeles Jets (ABL) LAL - Los Angeles Lakers (NBA) LAS - Los Angeles Stars (ABA) LBC - Long Beach Chiefs (ABL) LBS - Long Beach Stingrays (ABL) LOC - Louisville Colonels (PBLA) LOU - Louisville Alumnites (NPBL) LSP - Los Angeles Sparks (WNBA) MEG - Memphis Grizzlies (NBA) MEM - Memphis Pros/Memphis Tams/Memphis Sounds (ABA) MFD - Midland Dow A.C.'s/Flint Dow A.C.'s (NBL) MIA - Miami Heat (NBA) MIF - Miami Floridians (ABA) MIL - Milwaukee Bucks (NBA) MIN - Minnesota Timberwolves (NBA) MLD - Milwaukee Does (WBL) MLH - Milwaukee Hawks (NBA) MNF - Minnesota Fillies (WBL) MNL - Minnesota Lynx (WNBA) MNM - Minnesota Muskies (NBA) MNP - Minnesota Pipers (ABA) MPL - Minneapolis Lakers (NBL/BAA/NBA) NBW - Nebraska Wranglers (WBL) NEB - New England Blizzard (ABL) NEG - New England Gulls (WBL) NJA - New Jersey Americans (ABA) NJN - New Jersey Nets (NBA) NOB - New Orleans Buccaneers (ABA) NOH - New Orleans Hurricanes (PBLA) NOK - New Orleans/Oklahoma City Hornets (NBA) NOP - New Orleans Pride (WBL) NOR - New Orleans Jazz (NBA) NSH - Nashville Noise (ABL) NYC - New York Celtics (ABL) NYG - New Jersey Gems (WBL) NYH - New York Hakoahs (ABL) NYK - New York Knickerbockers (BAA/NBA) NYL - New York Liberty (WNBA) NYN - New York Nets (ABA/NBA) NYS - New York Stars (WBL) OAK - Oakland Oaks (ABA) OKD - Oklahoma City Drillers (PBLA) OKO - Oakland Oaks (ABL) OMA - Omaha Tomahawks (PBLA) ORL - Orlando Magic (NBA) ORM - Orlando Miracle (WNBA) OSH - Oshkosh All-Americans (NBL) PAC - Paterson Crescents (ABL) PAW - Paterson Whirlwinds (ABL) PHF - Philadelphia Fox (WBL) PHI - Philadelphia 76ers (NBA) PHM - Phoenix Mercury (WNBA) PHP - Philadelphia Phillies (ABL) PHR - Philadelphia Rage (ABL) PHT - Philadelphia Tapers (ABL) PHW - Philadelphia Warriors (BAA/NBA) PHX - Phoenix Suns (NBA) PIT - Pittsburgh Ironmen (BAA) POR - Portland Trailblazers (NBA) PRN - Pittsburgh Rens (ABL) PRO - Providence Steamrollers (BAA) PRT - Portland Power (ABL) PTC - Pittsburgh Pipers/Pittsburgh Condors (ABA) PTP - Pittsburgh Pirates (NBL) PTR - Pittsburgh Raiders (NBL) PWA - Philadelphia Warriors (ABL) RCC - Richmond King Clothiers/Cincinnati Comellos (NBL) RCH - Rochester Centrals (ABL) RIR - Richmond Rage (ABL) ROC - Rochester Royals (NBL/BAA/NBA) SAA - Syracuse All-Americans (ABL) SAC - Sacramento Kings (NBA) SAM - Sacramento Monarchs (WNBA) SAN - San Antonio Spurs (ABA/NBA) SDC - San Diego Clippers (NBA) SDR - San Diego Rockets (NBA) SDS - San Diego Conquistadors/Sails (ABA) SEA - Seattle Supersonics (NBA) SER - Seattle Reign (ABL) SFP - San Francisco Pioneers (WBL) SFS - San Francisco Saints (ABL) SFW - San Francisco Warriors (NBA) SHE - Sheboygan Redskins (NBL/NBA/NPBL) SJL - San Jose Lasers (ABL) SJO - St. Joseph Outlaws (PBLA) SLB - St. Louis Bombers (BAA/NBA) SLS - St. Louis Streak (WBL) SPL - St. Paul Lights (NPBL) SPR - Springfield Squires (PBLA) SPS - St. Paul Saints (PBLA) SST - Spirits of St. Louis (ABA) STL - St. Louis Hawks (NBA) SYR - Syracuse Nationals (NBL/NBA) TEX - Texas Chaparrals (ABA) TLC - Toledo Jim White Chevrolets (NBL) TLJ - Toledo Jeeps (NBL) TOR - Toronto Raptors (NBA) TRE - Trenton Bengals (ABL) TRH - Toronto Huskies (BAA) TRI - Tri-City Blackhawks/Tri-Cities Blackhawks (NBA/NBA includes Buffalo Bisons) TRM - Toledo Red Man Tobaccos (ABL) TUL - Tulsa Rangers (PBLA) USZ - Utah Starzz (WNBA) UTA - Utah Jazz (NBA) UTS - Utah Stars (ABA) VAN - Vancouver Grizzlies (NBA) VIR - Virginia Squires (ABA) WAM - Washington Metros (WBL) WAR - Warren Penns (NBL) WAS - Washington Bullets/Wizards (NBA) WAT - Waterloo Hawks (NBL/NBA/NPBL) WCA - Whiting Ciesar All-Americans (NBL) WNY - Washington Taper/New York Tapers (ABL) WPF - Washington Palace Five (ABL) WSC - Washington Capitals (BAA/NBA) WSH - Washington Caps (ABA) WSM - Washington Mystics (WNBA) WTP - Waterloo Pro-Hawks (PBLA) YNG - Youngstown Bears (NBL)"

    AllTeams = ['FTW', 'INO', 'CHS', 'TOT', 'DNN', 'NYK', 'TRI', 'AND', 'PHW', 'WAT', 'SHE', 'ROC', 'BLB', 'MNL', 'SYR', 'WSC', 'BOS', 'STB', 'MLH', 'STL', 'DET', 'CIN', 'LAL', 'CHP', 'SFW', 'CHZ', 'BAL', 'PHI', 'CHI', 'SDR', 'SEA', 'MIL', 'ATL', 'PHO', 'POR', 'CLE', 'BUF', 'HOU', 'GSW', 'KCO', 'CAP', 'NOJ', 'WSB', 'KCK', 'IND', 'NYN', 'DEN', 'SAS', 'NJN', 'SDC', 'UTA', 'DAL', 'LAC', 'SAC', 'CHH', 'MIA', 'ORL', 'MIN', 'VAN', 'TOR', 'WAS', 'MEM', 'NOH', 'CHA', 'NOK', 'OKC', 'BRK', 'NOP', 'CHO']


    all_teams_list = []

    temp_list = []
    for i in allTeams:
        temp_list.append(i)
        if i == ')':
            all_teams_list.append(''.join(temp_list))
            temp_list = []

    actual_team_list = []
    for team in all_teams_list:
        team_abbev = team[1:4]
        if str(team_abbev) in AllTeams:
            actual_team_list.append(team)

    print(len(actual_team_list))
    print(len(AllTeams))
    temp_abbrev_list = []
    temp_dict = {}
    list_of_temp_dicts = []

    for team in actual_team_list:
        abbrev_team = str(team).split('-')[0]
        full_team_name = str(team).split('-')[1]
        print(str(abbrev_team)[1:])
        print(str(full_team_name)[1:])
        list_of_temp_dicts.append({"TeamAbbrev":str(abbrev_team)[1:-1], "FullName":str(full_team_name)[1:]})

    print(list_of_temp_dicts)
