//Functionalizes the App to be used for directive
var nbaDataVizApp = angular.module('nbaDataVizApp', []);

//Core Controller Logic-handles user driven event responses-captures input, makes
//api calls, ingests incoming data and format data to be sent to graphing in diective


//Accsses the root of the angular app
angular.module('nbaDataVizApp')
.controller("nbaDataVizController", ['$scope', '$http', function ($scope, $http) {

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// ONLOAD THESE FUNCTIONS ARE CALLED
  ///////////////////////////////////////////////////////////////////////////////////////////

  //APP Wide data objects
  //All available DataColumns
  $scope.DataColumns = [{'CatAbbrev': 'Age', 'FullCatName': ' Age of Player at the start of February 1st of that season.'}, {'CatAbbrev': 'GS', 'FullCatName': ' Games Started'}, {'CatAbbrev': 'MP', 'FullCatName': ' Minutes Played Per Game'}, {'CatAbbrev': 'FG', 'FullCatName': ' Field Goals Per Game'}, {'CatAbbrev': 'FGA', 'FullCatName': ' Field Goal Attempts Per Game'}, {'CatAbbrev': 'FGPercent', 'FullCatName': ' Field Goal Percentage\n'}, {'CatAbbrev': '3P', 'FullCatName': '3 Point Field Goals Per Game'}, {'CatAbbrev': '3PA', 'FullCatName': '3 Point Field Goal Attempts Per Game'}, {'CatAbbrev': '3PPercent', 'FullCatName': '3 Point Field Goal Percentage\n'}, {'CatAbbrev': '2P', 'FullCatName': '2 Point Field Goals Per Game'}, {'CatAbbrev': '2PA', 'FullCatName': '2 Point Field Goal Attempts Per Game'}, {'CatAbbrev': '2PPercent', 'FullCatName': '2 Point Field Goal Percentage\n'}, {'CatAbbrev': 'eFGPercent', 'FullCatName': ' Effective Field Goal Percentage\n'}, {'CatAbbrev': 'FT', 'FullCatName': ' Free Throws Per Game'}, {'CatAbbrev': 'FTA', 'FullCatName': ' Free Throw Attempts Per Game'}, {'CatAbbrev': 'FTPercent', 'FullCatName': ' Free Throw Percentage\n'}, {'CatAbbrev': 'ORB', 'FullCatName': ' Offensive Rebounds Per Game'}, {'CatAbbrev': 'DRB', 'FullCatName': ' Defensive Rebounds Per Game'}, {'CatAbbrev': 'TRB', 'FullCatName': ' Total Rebounds Per Game'}, {'CatAbbrev': 'AST', 'FullCatName': ' Assists Per Game'}, {'CatAbbrev': 'STL', 'FullCatName': ' Steals Per Game'}, {'CatAbbrev': 'BLK', 'FullCatName': ' Blocks Per Game'}, {'CatAbbrev': 'TOV', 'FullCatName': ' Turnovers Per Game'}, {'CatAbbrev': 'PF', 'FullCatName': ' Personal Fouls Per Game'}, {'CatAbbrev': 'PTS', 'FullCatName': ' Points Per Game'}, {'CatAbbrev': 'PER', 'FullCatName': ' Player Efficency Rating'}, {'CatAbbrev': 'TSPercent', 'FullCatName': ' True Shooting Percentage'}, {'CatAbbrev': '3PAr', 'FullCatName': 'Point Attempt Rate'}, {'CatAbbrev': 'ORBPercent', 'FullCatName': ' Offensive Rebounds Per Game'}, {'CatAbbrev': 'DRBPercent', 'FullCatName': ' Defensive Rebound Percentage'}, {'CatAbbrev': 'TRBPercent', 'FullCatName': ' Total Rebound Percentage'}, {'CatAbbrev': 'ASTPercent', 'FullCatName': ' Assist Percentage'}, {'CatAbbrev': 'STLPercent', 'FullCatName': ' Steal Percentage'}, {'CatAbbrev': 'BLKPercent', 'FullCatName': ' Block Percentage'}, {'CatAbbrev': 'TOVPercent', 'FullCatName': ' Turnovers Percentage'}, {'CatAbbrev': 'USGPercent', 'FullCatName': ' Usage Percentage'}, {'CatAbbrev': 'OBPM', 'FullCatName': ' Offensive Box Plus/Minus'}, {'CatAbbrev': 'DBPM', 'FullCatName': ' Defensive Box Plus/Minus'}, {'CatAbbrev': 'BPM', 'FullCatName': ' Box Plus/Minus'}, {'CatAbbrev': 'OWS', 'FullCatName': ' Offensive Win Shares'}, {'CatAbbrev': 'DWS', 'FullCatName': ' Defensive Win Shares'}, {'CatAbbrev': 'WS', 'FullCatName': ' Win Shares'}, {'CatAbbrev': 'WS/48', 'FullCatName': ' Win Shares Per 48 Minutes'}]
  //All years of available data
  $scope.allYears = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'];
  //Long List of All Teams
  $scope.AllTeams = [{'TeamAbbrev': 'AND', 'FullName': 'Anderson Duffey Packers/Anderson Packers (NBL/NBA/NPBL)'}, {'TeamAbbrev': 'ATL', 'FullName': 'Atlanta Hawks (NBA)'}, {'TeamAbbrev': 'BAL', 'FullName': 'Baltimore Bullets (NBA)'}, {'TeamAbbrev': 'BLB', 'FullName': 'Baltimore Bullets (ABL/BAA/NBA)'}, {'TeamAbbrev': 'BOS', 'FullName': 'Boston Celtics (BAA/NBA)'}, {'TeamAbbrev': 'BUF', 'FullName': 'Buffalo Braves (NBA)'}, {'TeamAbbrev': 'CAP', 'FullName': 'Capital Bullets (NBA)'}, {'TeamAbbrev': 'CHA', 'FullName': 'Charlotte HorNBA (NBA)'}, {'TeamAbbrev': 'CHH', 'FullName': 'Chicago Hustle (WBL)'}, {'TeamAbbrev': 'CHI', 'FullName': 'Chicago Bulls (NBA)'}, {'TeamAbbrev': 'CHO', 'FullName': 'Charlotte HorNBA (Post-2016)'}, {'TeamAbbrev': 'CHP', 'FullName': 'Chicago Packers/Zephyrs (NBA)'}, {'TeamAbbrev': 'CHS', 'FullName': 'Chicago Stags (BAA/NBA)'}, {'TeamAbbrev': 'CIN', 'FullName': 'Cincinnati Royals (NBA)'}, {'TeamAbbrev': 'CLE', 'FullName': 'Cleveland Cavaliers (NBA)'}, {'TeamAbbrev': 'SAS', 'FullName': 'San Antonio Spurs (NBA)'}, {'TeamAbbrev': 'PHO', 'FullName': 'Phoenix Suns (NBA)'}, {'TeamAbbrev': 'DAL', 'FullName': 'Dallas Mavericks (NBA)'}, {'TeamAbbrev': 'DEN', 'FullName': 'Denver Rockets/Nuggets (ABA/NBA)'}, {'TeamAbbrev': 'DET', 'FullName': 'Detroit Pistons (NBA)'}, {'TeamAbbrev': 'FTW', 'FullName': 'Fort Wayne Zollner Pistons/Fort Wayne Pistons (NBL/BAA/NBA)'}, {'TeamAbbrev': 'HOU', 'FullName': 'Houston Rockets (NBA)'}, {'TeamAbbrev': 'IND', 'FullName': 'Indiana Pacers (ABA/NBA)'}, {'TeamAbbrev': 'INO', 'FullName': 'Indianapolis Olympians (NBA)'}, {'TeamAbbrev': 'KCK', 'FullName': 'Kansas City Kings (NBA)'}, {'TeamAbbrev': 'KCO', 'FullName': 'Kansas City'}, {'TeamAbbrev': 'LAC', 'FullName': 'Los Angeles Clippers (NBA)'}, {'TeamAbbrev': 'LAL', 'FullName': 'Los Angeles Lakers (NBA)'}, {'TeamAbbrev': 'MEM', 'FullName': 'Memphis Grizzlies (NBA)'}, {'TeamAbbrev': 'MIA', 'FullName': 'Miami Heat (NBA)'}, {'TeamAbbrev': 'MIL', 'FullName': 'Milwaukee Bucks (NBA)'}, {'TeamAbbrev': 'MIN', 'FullName': 'Minnesota Timberwolves (NBA)'}, {'TeamAbbrev': 'MLH', 'FullName': 'Milwaukee Hawks (NBA)'}, {'TeamAbbrev': 'MNL', 'FullName': 'Minnesota Lynx (WNBA)'}, {'TeamAbbrev': 'NJN', 'FullName': 'New Jersey Nets (NBA)'}, {'TeamAbbrev': 'NOH', 'FullName': 'New Orleans HorNBA (NBA)'}, {'TeamAbbrev': 'NOK', 'FullName': 'New Orleans/Oklahoma City HorNBA (NBA)'}, {'TeamAbbrev': 'NOP', 'FullName': 'New Orleans Pelicans (NBA)'}, {'TeamAbbrev': 'NYK', 'FullName': 'New York Knickerbockers (BAA/NBA)'}, {'TeamAbbrev': 'BRK', 'FullName': 'Brooklyn NBA (NBA)'}, {'TeamAbbrev': 'ORL', 'FullName': 'Orlando Magic (NBA)'}, {'TeamAbbrev': 'PHI', 'FullName': 'Philadelphia 76ers (NBA)'}, {'TeamAbbrev': 'PHW', 'FullName': 'Philadelphia Warriors (BAA/NBA)'}, {'TeamAbbrev': 'POR', 'FullName': 'Portland Trailblazers (NBA)'}, {'TeamAbbrev': 'ROC', 'FullName': 'Rochester Royals (NBL/BAA/NBA)'}, {'TeamAbbrev': 'SAC', 'FullName': 'Sacramento Kings (NBA)'}, {'TeamAbbrev': 'SDC', 'FullName': 'San Diego Clippers (NBA)'}, {'TeamAbbrev': 'SDR', 'FullName': 'San Diego Rockets (NBA)'}, {'TeamAbbrev': 'SEA', 'FullName': 'Seattle Supersonics (NBA)'}, {'TeamAbbrev': 'SFW', 'FullName': 'San Francisco Warriors (NBA)'}, {'TeamAbbrev': 'GSW', 'FullName': 'Golden State Warriors (NBA)'}, {'TeamAbbrev': 'SHE', 'FullName': 'Sheboygan Redskins (NBL/NBA/NPBL)'}, {'TeamAbbrev': 'STL', 'FullName': 'St. Louis Hawks (NBA)'}, {'TeamAbbrev': 'SYR', 'FullName': 'Syracuse Nationals (NBL/NBA)'}, {'TeamAbbrev': 'TOR', 'FullName': 'Toronto Raptors (NBA)'}, {'TeamAbbrev': 'TRI', 'FullName': 'Tri'}, {'TeamAbbrev': 'UTA', 'FullName': 'Utah Jazz (NBA)'}, {'TeamAbbrev': 'VAN', 'FullName': 'Vancouver Grizzlies (NBA)'}, {'TeamAbbrev': 'WAS', 'FullName': 'Washington Bullets/Wizards (NBA)'}, {'TeamAbbrev': 'WAT', 'FullName': 'Waterloo Hawks (NBL/NBA/NPBL)'}, {'TeamAbbrev': 'WSC', 'FullName': 'Washington Capitals (BAA/NBA)'}];

  //Gets a list of all players
  function GetAllPlayerToPopulateDataList() {
    $scope.AllPlayers = [];
    $http.post('/get_individual_column', {"columnName": "Player"})
    .then(function(results) {
      $scope.AllPlayers = results.data;
    });
  };

  //To be used in onLoad-which is why it's outside of a scope function
  //Launches api call and sends data to directive
  function categoryOverTeamExistence(category, team) {
    //Make a post call to the server/database to get player data
    $http.post('/category_over_team_existence', {"category":category.CatAbbrev, "team":team.TeamAbbrev})
    .then(function(results) {
      //Sends player info to Directive
      $scope.playerData = [category, team.FullName, results.data];
    });
  };//End playerStatsOverCareer

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// END ONLOAD
  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// Player Data Acquisition
  ///////////////////////////////////////////////////////////////////////////////////////////

  $scope.GraphPlayer = function GraphPlayer() {
    //Shows fields now that GraphPlayer() has been selected
    d3.select("div#playerSelection")
      .style("visibility", "visible");
    d3.select("ul#selectionHolder")
      .style("visibility", "visible");

    //Fires when player data is entered
    $scope.PlayerSelected = function PlayerSelected(PlayerSelected){
      //cycles through the list of player names and when they match with chosen
      //player, PlayerToUse is sent to scope
      var PlayerToUse = [];
      for (var eachPlayer in $scope.AllPlayers) {
        if ($scope.AllPlayers[eachPlayer] == PlayerSelected) {
            PlayerToUse.push($scope.AllPlayers[eachPlayer]);
        }};
        //If theres a whole name
        if (PlayerToUse.length >= 1) {
          //if the newly selected player equals the whole name
          if (PlayerToUse[0] == PlayerSelected) {
            //Asigns the newly selected player to the scope
            $scope.currentPlayerToUSE = PlayerToUse[0];
            //If the player object exists then triggers the redrawing of the new graph
            if ($scope.PlayerStatCategory) {
              //Tiggers API call and sends returnd data to directive
              playerStatsOverCareer($scope.PlayerStatCategory, $scope.currentPlayerToUSE)
            };
          }
        };
      };

    //Gets a players performance in any stat category for every year they played
    $scope.PlayerStatCategorySelector = function PlayerStatCategorySelector(PlayerStatCategory) {
      PlayerStatCategory = JSON.parse(PlayerStatCategory);
      $scope.PlayerStatCategory = PlayerStatCategory;
      //If a player is selected
      if ($scope.currentPlayerToUSE) {
        if ($scope.PlayerStatCategory) {
          //Tiggers API call and sends returnd data to directive
          playerStatsOverCareer($scope.PlayerStatCategory, $scope.currentPlayerToUSE);
        }
      }
    };

    //Launches api call and sends data to directive
    function playerStatsOverCareer(category, player) {
      //Make a post call to the server/database to get player data
      $http.post('/category_over_player_career', {"category":category.CatAbbrev, "player":player})
      .then(function(results) {
        //Sends player info to Directive
        $scope.playerData = [category, player, results.data];
      });
    };//End playerStatsOverCareer
  };//End Graph player

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// END Graph player
  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// TEAM Data Acquisition
  ///////////////////////////////////////////////////////////////////////////////////////////

  //fires when th Graph team button is selected
  $scope.GraphTeam = function GraphTeam() {
    //Shows fields now that GraphTeam() has been selected
    d3.select("div#teamSelection")
      .style("visibility", "visible");
    d3.select("ul#selectionHolder")
      .style("visibility", "visible");

    $scope.TeamSelected = function TeamSelected(Team){
      //cycles through the list of player names and when they match with chosen
      //team, TeamToUse is sent to scope
      var TeamToUse = [];
      $scope.AllTeams.forEach(function(teamName) {
        if (teamName.FullName == Team) {
          TeamToUse.push(teamName);
          };
        });
        //If theres a whole team name
        if (TeamToUse.length >= 1) {
          //if the newly selected team equals the whole name
          if (TeamToUse[0].FullName == Team) {
            //Asigns the newly selected team to the scope
            $scope.currentTeamToUSE = TeamToUse[0];
            //If the player object exists then triggers the redrawing of the new graph
            if ($scope.TeamStatCategory) {
              //Tiggers API call and sends returnd data to directive
              categoryOverTeamExistence($scope.TeamStatCategory, $scope.currentTeamToUSE)
            };
          }
        };
      };

      //Gets a players performance in any stat category for every year they played
      $scope.TeamStatCategorySelector = function TeamStatCategorySelector(TeamStatCategory) {
        TeamStatCategory = JSON.parse(TeamStatCategory);
        $scope.TeamStatCategory = TeamStatCategory;
        //If a player is selected
        if ($scope.currentTeamToUSE) {
          if ($scope.TeamStatCategory) {
            //Tiggers API call and sends returnd data to directive
            categoryOverTeamExistence($scope.TeamStatCategory, $scope.currentTeamToUSE);
          }
        }
      };
    };

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// END Graph TEAM
  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// YEAR Data Acquisition
  ///////////////////////////////////////////////////////////////////////////////////////////

  //fires when th Graph year button is selected
  $scope.GraphYear = function GraphYear() {
    //Shows fields now that GraphYear() has been selected
    d3.select("div#yearSelection")
      .style("visibility", "visible");
    d3.select("ul#selectionHolder")
      .style("visibility", "visible");

    $scope.YearSelected = function YearSelected(Year){
      if (Year) {
        //Asigns the newly selected year to the scope
        $scope.currentYearToUSE = Year;
        //If the player object exists then triggers the redrawing of the new graph
        if ($scope.YearStatCategory) {
          //Tiggers API call and sends returnd data to directive
          top20PlayersInCategoryForYear($scope.YearStatCategory, $scope.currentYearToUSE)
        };
      }
    };

    //Gets a players performance in any stat category for every year they played
    $scope.YearStatCategorySelector = function YearStatCategorySelector(YearStatCategory) {
      YearStatCategory = JSON.parse(YearStatCategory);
      $scope.YearStatCategory = YearStatCategory;
      //If a player is selected
      if ($scope.currentYearToUSE) {
        if ($scope.YearStatCategory) {
          //Tiggers API call and sends returnd data to directive
          top20PlayersInCategoryForYear($scope.YearStatCategory, $scope.currentYearToUSE);
        }
      }
    };

    function top20PlayersInCategoryForYear(category, year) {
      $http.post('/top_20_players_in_category_for_year', {"category":category.CatAbbrev, "year":year})
      .then(function(results) {
        $scope.playerData = [category, year, results.data];
      });
    };
  };

  ///////////////////////////////////////////////////////////////////////////////////////////
  ///////////// END Graph YEAR
  ///////////////////////////////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////////////////////////////

  //Functions to be run onLoad
  function init() {
    //Loads Data initially
    GetAllPlayerToPopulateDataList();
    //Loads a chart when the page is first loaded
    categoryOverTeamExistence({'CatAbbrev': '3P', 'FullCatName': '3 Point Field Goals Per Game'}, {'TeamAbbrev': 'NJN', 'FullName': 'New Jersey Nets (ABA/NBA)'});

    console.log('Helllo');
    //Hides playerSelection until the Graph Player Option is slected
    d3.select("div#playerSelection")
      .style("visibility", "hidden");
    d3.select("div#teamSelection")
      .style("visibility", "hidden");
    d3.select("div#yearSelection")
      .style("visibility", "hidden");
    d3.select("ul#selectionHolder")
      .style("visibility", "hidden");

  };
//Launches functions onLoad
init();
}]);
