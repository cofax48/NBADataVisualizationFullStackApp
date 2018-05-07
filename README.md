A Data Viz App for all NBA Stats Ever!
Within this directory there are two folders: The DockerNGINXFlask folder contains the Dockerized version of this project wherein the app is orchestrated with Docker-Compose, runs on Flask, served with NGINX for proxying/load balancing/serving and connects to the Postgres DB. When composed, the app will be available http://localhost:8080/.

While the DjangoHeroku folder contains the Django implementation of the project which is currently deployed to Heroku and is accessible now at https://nba-data-viz-app.herokuapp.com/

The Aims/Goals: This project aims to bring 67 years of player statistics to life in an easy to use and easy to visualize manner. The goal was also to build a full-stack web app using open source technologies and to deploy into production/Dockerization. This was successfully accomplished. User interaction is designed to choose between graphing stats by player for each year they played. Averaged Stats for each team for each year records are available. And by individual year, where the top 20 preforming players in that category have their records visualized.

The Data: Data was acquired from https://www.kaggle.com/drgilermo/nba-players-stats/version/1, In this data set are player stats for every NBA player, for every year they played professional basketball, with all available statistical categories for the years in which they played. I.e. Wilt Chamberlain does not have any 3pt Stats because he played (59-73) prior to the creation off the three point line in 1979.

The Database Postgres was employed because its scalable, open-source, works on Heroku/Docker, and is overall terrific! In both projects I opt to execute raw SQL over ORMs, I do so mainly because I like writing SQL and I find it easier to debug SQL statements then ORM models, just a personal preference and I'm far from dogmatic about it.

Both projects employ a PostgresDB and use the same front-end so the only variation is within the backend.

A Separate README for DjangoHeroku and DockerNGINXFlask implementations are found in their respective folders

FrontEnd, SPA: The frontend is built with AngularJS, which handles user input from the html, handles API calls, formats incoming data, and segments user interaction into the controller and the directive (which handles the visualization). Controller: /NBADataVisualizationFullStackApp/DockerNGINXFlask/static/assets/js/NBADataVizController.js

Data Visualization: D3.js is the heavy hitter in the data visualization space and a bar chart was chosen from the d3 graphical offerings as its simple and easy to infer, especially considering the nature of data set. D3 is used to generate all graphs, tooltips, writing and any other features associated with the visualization. D3 Directive: /NBADataVisualizationFullStackApp/DockerNGINXFlask/static/assets/js/NBADataVizDirective.js

CSS3/HTML5: I employed previously written CSS code to format the basic design of the app and to format for a variety of mobile scenarios. I additionally wrote new css for certain graphing aspects. CSS: /NBADataVisualizationFullStackApp/DockerNGINXFlask/static/assets/css/main.css Html: /NBADataVisualizationFullStackApp/DockerNGINXFlask/templates/Homepage.html

-Josh
