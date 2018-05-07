//Data Visualization Directive-where the D3 magic happens

nbaDataVizApp.directive('nbadataViz', function(){
  function link(scope, element, attr){
    scope.$watch('data', function(data){
      //removes pevious initializations
      d3.select("div#GraphNBAD3").selectAll("*").remove();
      d3.selectAll("div.tooltip").remove();
      //If data has arived at the directive
      if (data) {
        //Formats incoming data
        var category = data[0];
        var secondParam = data[1];
        data = data[2];

        //if secondParam is a year then its top 20 players and theres different formatting
        if (1949 < Number(secondParam)) {

          //sorts data so all years are in order
          data = data.sort((a, b) => parseFloat(Number(a[category.CatAbbrev])) - parseFloat(Number(b[category.CatAbbrev])));

          // set the dimensions and margins of the graph
          var margin = {top: 7, right: 20, bottom: 120, left: 20},
              width = 1160 - margin.left - margin.right,
              height = 500 - margin.top - margin.bottom;

          // creates the svg element
          var svg = d3.select("div#GraphNBAD3").append("svg")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
            .append("g")
              .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

          var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
              y = d3.scaleLinear().rangeRound([height, 0]);

          var g = svg.append("g")
              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            x.domain(data.map(function(d) { return d.Player; }));
            y.domain([d3.min(data, function(d) { return Number(Number(d[category.CatAbbrev]) * .5); }), d3.max(data, function(d) { return Number(Number(d[category.CatAbbrev]) * 1.2); })]);

            //Makes the bars themeseleves
            var bars = g.selectAll(".bar")
              .data(data)
              .enter().append("rect")
                .attr("class", "bar")
                .attr("x", function(d) { return x(d.Player); })
                .attr("y", function(d) { return y(Number(d[category.CatAbbrev])); })
                .attr("width", x.bandwidth())
                .attr("height", function(d) { return height - y(Number(d[category.CatAbbrev])); });

                // Define the div for the tooltip
                var div = d3.select("body").append("div")
                    .attr("class", "tooltip")
                    .style("opacity", 0);

                //Adds the tooltip to each bar
                bars
                  .on("mouseover", function (d) {
                            div.transition()
                                .duration(200)
                                .style("opacity", .9);

                            //Makes the number only two digits past decimal
                            var num = Number(d[category.CatAbbrev]);
                            div.html("In " + String(secondParam) + " " + d.Player + "<br/>" + " recorded " + d[category.CatAbbrev] + ' ' + String(category.CatAbbrev))
                                .style("left", (d3.event.pageX) + "px")
                                .style("top", (d3.event.pageY - 28) + "px")
                                .style("color", "black");
                      d3.select(this).style("stroke-opacity", 1.0);
                      div.style("visibility", "visible");
                  })
                  .on("mouseout", function () {
                      d3.select(this).style("stroke-opacity", 0.0);
                      div.style("visibility", "hidden");
                  });
        }
        //If the x axis is not players
        else {

          // set the dimensions and margins of the graph
          var margin = {top: 7, right: 20, bottom: 55, left: 20},
              width = 1160 - margin.left - margin.right,
              height = 500 - margin.top - margin.bottom;

          // creates the svg element
          var svg = d3.select("div#GraphNBAD3").append("svg")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
            .append("g")
              .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

          var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
              y = d3.scaleLinear().rangeRound([height, 0]);

          var g = svg.append("g")
              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

          //sorts data so all years are in order
          data = data.sort((a, b) => parseFloat(a.Year) - parseFloat(b.Year));

          x.domain(data.map(function(d) { return Number(d.Year); }));
          y.domain([d3.min(data, function(d) { return Number(Number(d[category.CatAbbrev]) * .5); }), d3.max(data, function(d) { return Number(Number(d[category.CatAbbrev]) * 1.2); })]);

          // Define the div for the tooltip
          var div = d3.select("body").append("div")
              .attr("class", "tooltip")
              .style("opacity", 0);

          //Makes the bars themeseleves
          var bars = g.selectAll(".bar")
            .data(data)
            .enter().append("rect")
              .attr("class", "bar")
              .attr("x", function(d) { return x(Number(d.Year)); })
              .attr("y", function(d) { return y(Number(d[category.CatAbbrev])); })
              .attr("width", x.bandwidth())
              .attr("height", function(d) { return height - y(Number(d[category.CatAbbrev])); });

          //Adds the tooltip to each bar
          bars
            .on("mouseover", function (d) {
                      div.transition()
                          .duration(200)
                          .style("opacity", .9);

                      //removes the NBA/ABA
                      var AbbrevSecondParam = String(secondParam).split('(')[0];
                      //Makes the number only two digits past decimal
                      var num = Number(d[category.CatAbbrev]);
                      if (String(secondParam).indexOf('(') > -1)
                        {
                          //If team the div tooltip says averaged
                          div.html("In " + d.Year + " the " + AbbrevSecondParam + "<br/>" + " averaged " + num.toFixed(2) + ' ' + String(category.FullCatName))
                              .style("left", (d3.event.pageX) + "px")
                              .style("top", (d3.event.pageY - 28) + "px")
                              .style("color", "black");
                        } else {
                          //If player the div tooltip says averaged
                          div.html("In " + d.Year + " " + AbbrevSecondParam + "<br/>" + " recorded " + num.toFixed(2) + ' ' + String(category.FullCatName))
                              .style("left", (d3.event.pageX) + "px")
                              .style("top", (d3.event.pageY - 28) + "px")
                              .style("color", "black");
                      };
                d3.select(this).style("stroke-opacity", 1.0);
                div.style("visibility", "visible");
            })
            .on("mouseout", function () {
                d3.select(this).style("stroke-opacity", 0.0);
                div.style("visibility", "hidden");
            });

        };//if not year

      ////////////////////////////////////////////////////
      //////// Formatting applicable to both graphs
      ////////////////////////////////////////////////////

      //X Axis
      g.append("g")
          .attr("class", "axis axis--x")
          .style("stroke", "#ffffff")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x))
          .selectAll("text")
          .style("text-anchor", "end")
          .style("font-size", "14px")
          .style("color", "#ffffff")
          .attr("dx", "-.8em")
          .attr("dy", ".15em")
          .attr("transform", function(d) {
              return "rotate(-65)"
              });

      //Y axis
      g.append("g")
          .attr("class", "axis axis--y")
          .style("stroke", "#ffffff")
          .call(d3.axisLeft(y).ticks(10))
        .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .style("font-size", "14px")
          .style("color", "#ffffff")
          .attr("dy", "0.51em")
          .attr("text-anchor", "end")
          .text(category.FullCatName);

      //Title
      g.append("text")
        .attr("class", "title")
        .style("fill", "#ffffff")
        .style("stroke-linecap", "round")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top - 30))
        .attr("text-anchor", "middle")
        .style("font-size", "20px")
        .style("text-decoration", "underline")
        .text("Stats for " + String(secondParam) + " by " + String(category.FullCatName) );

          };//If data
        }, true); // Watcher
      }//Link function
      return {
        link: link,
        restrict: 'E',
        scope: { data: '=' }
      }
});
