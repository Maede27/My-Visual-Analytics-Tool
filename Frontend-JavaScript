<!DOCTYPE html>
<!--<div>-->

<head>
    <meta charset="utf-8">
    <title>Visual Analytics System</title>
    <script src="/static/js/d3.v3.min.js" charset="utf-8"></script>
    <script src="/static/js/jquery.min.js" charset="utf-8"></script>
<!--        background-image: url('https://lh3.googleusercontent.com/proxy/');-->
    <style>
    body {
background-image: url('https://momentumchoir.ca/wp-content/uploads/2017/01/Geometric-Header-White-Overlay.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
    }
    .bar_1 {
            fill: #03923E;
            opacity: 0.8;
            display: grid;
        }

        .axis path,
        .axis line {
            fill: none;
            stroke: #000;
            shape-rendering: crispEdges;
        }

        h1 {
            text-align: left;
            margin-top: 10px;
            margin-bottom: 0px;
            margin-left: 30px;
            font-family: Cursive;
            font-size: 14px;
        }
    }
    .bar_1: hover {
        fill: green;
    }
    input {
        width: 1.2em;
        height: 1.2em;
        margin: 19px;
        margin-top: 2px;
        margin-bottom: 2px;
        background-color: white;
        border-color: black;
        border: 2px solid #e4e4e4;
    }
    .mutual {
        background-color: white;
        color: black;
        font-size: 15px;
        font-family: Cursive;
        border-color: black;
        border-radius: 4em;
        margin-top: 0px;
        margin-bottom: 0px;
        margin-left: 5px;
    }
    .mutual:hover {
        background-color: white;
        color: blacke;
    }
    #box1 {
        margin-top: 20px;
        margin-bottom: 0px;
        margin-left: 60px;
        margin-right: 100px;
<!--        background-color: lightyellow;-->
        border-color: black;
    }
    #box2 {
        margin-top: 1px;
        margin-bottom: 0px;
        margin-left: 60px;
        margin-right: 100px;
    }
    #box3 {
        margin-top: 1px;
        margin-bottom: 20px;
        margin-left: 60px;
        margin-right: 100px;
    }
    #selectage {
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 3px;
        margin-left: 8px;
    }
    #selectsex {
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 3px;
        margin-left: 8px;
    }
    #selectsocioeconomic {
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 3px;
        margin-left: 8px;
    }

    #BarChartType {
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 3px;
        margin-left: 8px;
    }
    #MatrixType {
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 3px;
        margin-left: 8px;
    }
    #button1 {
        font-size: 15px;
        margin-top: 10px;
        margin-bottom: 3px;
        margin-left: 10px;
        color: red;
    }
<!--    body {-->
<!--        background: #f2f2f2;-->
<!--    }-->
    text {
        fill: #803300;
        font-family: Arial Narrow, Arial, sans-serif;
        text-align: center;
        font-size: 11.6px;
    }
    <!--#title {
        --> <!--margin-top: 0px;
        --> <!--margin-bottom: 0px;
        --> <!--margin-left: 30px;
        --> <!--font-family: Cursive;
        --> <!--font-size: 14px;
        --> <!--
    }
    .container1 {
        float: left;
    }
    .container2 {
        float: right;
    }
    --> //################################################
    //matrix_style.css# *******
    @font-face {
        font-family: 'PT Sans';
        font-style: normal;
        font-weight: 400;
        unicode-range: U+0460-052F, U+20B4, U+2DE0-2DFF, U+A640-A69F;
    }
    .ocks-org {
        background: white;
        color: #333;
        font-family: "PT Serif", serif;
        margin-top: 1px;
        margin-bottom: 1px;
        margin-left: 50px;
    }
    .background {
        fill: #eee;
    }
    line {
        stroke: #fff;
    }
    text.active {
        fill: red;
    }
    .attribution {
        font-size: large;
        margin-bottom: 2em;
    }
    body > p,
    li > p {
        line-height: 1.5em;
    }
    body > p {
        width: 720px;
    }
    body > blockquote {
        width: 640px;
    }
    blockquote q {
        display: block;
        font-style: oblique;
    }
    ul {
        padding: 0;
    }
    li {
        width: 690px;
        margin-left: 30px;
    }
    a {
        color: steelblue;
    }
    a:not(:hover) {
        text-decoration: none;
    }
    pre,
    code,
    textarea {
        font-family: "Menlo", monospace;
    }
    code {
        line-height: 1em;
    }
    textarea {
        font-size: 100%;
    }
    body > pre {
        border-left: solid 2px #ccc;
        padding-left: 18px;
        margin: 2em 0 2em -20px;
    }
    .html .value,
    .javascript .string,
    .javascript .regexp {
        color: #756bb1;
    }
    .html .tag,
    .css .tag,
    .javascript .keyword {
        color: #3182bd;
    }
    .comment {
        color: #636363;
    }
    .html .doctype,
    .javascript .number {
        color: #31a354;
    }
    .html .attribute,
    .css .attribute,
    .javascript .class,
    .javascript .special {
        color: #e6550d;
    }
    .axis path,
    .axis line {
        fill: none;
        stroke: #000;
        shape-rendering: crispEdges;
    }
    sup,
    sub {
        line-height: 0;
    }
    q:before {
        content: "“";
    }
    q:after {
        content: "”";
    }
    blockquote q {
        line-height: 1.5em;
        display: inline;
    }
    blockquote q:before,
    blockquote q:after {
        content: "";
    }
    #tooltip {
        z-index: 9999;
        position: absolute;
        width: 200px;
        height: auto;
        padding: 10px;
        background-color: white;
        -webkit-border-radius: 10px;
        -moz-border-radius: 10px;
        border-radius: 10px;
        -webkit-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
        -moz-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
        pointer-events: none;
    }
    #tooltip.hidden {
        display: none;
    }
    #tooltip p {
        margin: 0;
        font-family: sans-serif;
        font-size: 12px;
        line-height: 10px;
    }
    </style>
</head>

<table style="width:100%;">
    <tr>
        <td>
            <select id="selectage" class="mutual" onchange="window.fn2()">
                <option value="100">Age Not Selected</option>
                <option value="2">Child and Young Adult</option>
                <option value="3">Adult and Middle-Aged</option>
                <option value="4">Elder</option>
            </select>

            <select id="selectsex" class="mutual" onchange="window.fn2() ">
                <option value="99">Gender Not Selected</option>
                <option value="1">Female</option>
                <option value="0">Male</option>
            </select>

            <select id="selectsocioeconomic" class="mutual" onchange="window.fn2()">
                <option value="101">Income Not Selected</option>
                <option value="0">Less than $50600</option>
                <option value="1">More than $50600</option>
            </select>


            <select id="BarChartType" class="mutual" onchange="window.fn2()">
                <option value="1">Count-Based Bar Chart</option>
                <option value="2">Decision-Tree-Based Bar Chart</option>
                <option value="3">Logistic-Regression-Based Bar Chart</option>
            </select>


            <select id="MatrixType" class="mutual" onchange="window.fn2()">
                <option value="1">Decision-Tree-Based Matrix</option>
                <option value="2">Softmax-Regression-Based Matrix</option>
            </select>

            <button class="mutual" id="button1" onclick="window.fn2()">Run</button>

            <aside style="margin-top:3px; margin-left:30px; margin-right:1155px; background: white" class="mutual">
                <p>Ordering The Matrix By:
                    <select id="order" class="mutual">
                        <option value="name">Name </option>
                        <option value="count">Correlation Value </option>
                        <!--                        <option value="group">Cluster </option>-->
                    </select>
            </aside>

            <!--                  //An empty header using for sample size text-->
            <h1 id="Header"></h1>

        </td>
    </tr>
</table>

<!--            <img src="https://www.uwo.ca/web_standards/img/icn/svg/western-stack.svg"-->
<!--                 alt="UWO Logo" width="200" height="200" style="float:right;">-->

<!--    <div id='title'></div>-->
<!--            <script type="text/javascript">-->

<!--                // set the title of the graph-->
<!--                 d3.select("#title").append("h1").text("Visualizing High-Dimensional Joint Distributions of Chronic Diseases");-->
<!--                 d3.select("#title").append("h2").text("Western University");-->
<!--            </script>-->

<div class="container1" id='vis-container1'></div>
<!--    <table id="tblOne" style="width:50%; float:left">-->
<!--        <tr>-->
<!--            <td>-->
<script>
    // To print the updated sample size every time
    textfunction = function(case_count) {
        d3.select("#Header").text("The sample size is:  " + case_count);
    };

    // var fileName2 = "./probability_dataset_five_disease.csv",
    diseases = ["HyperTens", "Diabetes", "Bronchitis", "HyperLip", "Cancer",
        "CardioVas", "Depression", "Arthritis", "Thyroid", "MusculoSkel"
    ];

    // Define dimensions of vis
    var margin = {
            top: 80,
            right: 150,
            bottom: 20,
            left: 50
        },
        width = 800 - margin.left - margin.right,
        height = 360 - margin.top - margin.bottom;

    // Make x scale
    var xScale = d3.scale.ordinal()
        .domain(diseases)
        .rangeRoundBands([0, width], 0.2);

    // Make y scale, the domain will be defined on bar update
    var yScale = d3.scale.linear()
        .range([height, 0]);

    var makeVis_1 = function() {

        // Create canvas
        var chart2 = d3.select("#vis-container1")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // Make x-axis and add to canvas
        var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");

        chart2.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        // Make y-axis and add to canvas
        var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");

        var yAxisHandleForUpdate = chart2.append("g")
            .attr("class", "y axis")
            .call(yAxis);

        yAxisHandleForUpdate.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Probability");

        var updateBars2 = function(data) {

            // First update the y-axis domain to match data
            yScale.domain([0, 1]);
            yAxisHandleForUpdate.call(yAxis);

            var bars = chart2.selectAll(".bar_1").data(data);

            // Add bars for new data
            bars.enter()
                .append("rect")
                .attr("class", "bar_1")
                .attr("x", function(d, i) {
                    return xScale(diseases[i]);
                })
                .attr("width", xScale.rangeBand())
                .attr("y", function(d, i) {
                    return yScale(d);
                })
                .attr("height", function(d, i) {
                    return height - yScale(d);
                });

            // Update old ones, already have x / width from before
            bars
                .transition().duration(700)
                .attr("y", function(d, i) {
                    return yScale(d);
                })
                .attr("height", function(d, i) {
                    return height - yScale(d);
                });

            // Remove old ones
            bars.exit().remove();

        };
        window.fn2 = function() {

            var rad1 = document.getElementById("rad1");
            var rad2 = document.getElementById("rad2");
            var rad3 = document.getElementById("rad3");
            var rad4 = document.getElementById("rad4");
            var rad5 = document.getElementById("rad5");
            var rad6 = document.getElementById("rad6");
            var rad7 = document.getElementById("rad7");
            var rad8 = document.getElementById("rad8");
            var rad9 = document.getElementById("rad9");
            var rad10 = document.getElementById("rad10");
            var rad11 = document.getElementById("rad11");
            var rad12 = document.getElementById("rad12");
            var rad13 = document.getElementById("rad13");
            var rad14 = document.getElementById("rad14");
            var rad15 = document.getElementById("rad15");
            var rad16 = document.getElementById("rad16");
            var rad17 = document.getElementById("rad17");
            var rad18 = document.getElementById("rad18");
            var rad19 = document.getElementById("rad19");
            var rad20 = document.getElementById("rad20");
            var rad21 = document.getElementById("rad21");
            var rad22 = document.getElementById("rad22");
            var rad23 = document.getElementById("rad23");
            var rad24 = document.getElementById("rad24");
            var rad25 = document.getElementById("rad25");
            var rad26 = document.getElementById("rad26");
            var rad27 = document.getElementById("rad27");
            var rad28 = document.getElementById("rad28");
            var rad29 = document.getElementById("rad29");
            var rad30 = document.getElementById("rad30");

            var d1 = 99;
            var d2 = 99;
            var d3 = 99;
            var d4 = 99;
            var d5 = 99;
            var d6 = 99;
            var d7 = 99;
            var d8 = 99;
            var d9 = 99;
            var d10 = 99;
            var age_val;
            var sex_val;
            var socioeconomic_val;
            var charttype_val;
            var matrixtype_val;

            age_val = document.getElementById("selectage").value;
            sex_val = document.getElementById("selectsex").value;
            socioeconomic_val = document.getElementById("selectsocioeconomic").value;
            charttype_val = document.getElementById("BarChartType").value
            matrixtype_val = document.getElementById("MatrixType").value

            if (rad1.checked == true) {
                d1 = 1;
            };
            if (rad2.checked == true) {
                d2 = 1;
            };
            if (rad3.checked == true) {
                d3 = 1;
            };
            if (rad4.checked == true) {
                d4 = 1;
            };
            if (rad5.checked == true) {
                d5 = 1;
            };
            if (rad6.checked == true) {
                d6 = 1;
            };
            if (rad7.checked == true) {
                d7 = 1;
            };
            if (rad8.checked == true) {
                d8 = 1;
            };
            if (rad9.checked == true) {
                d9 = 1;
            };
            if (rad10.checked == true) {
                d10 = 1;
            };
            if (rad11.checked == true) {
                d1 = 0;
            };
            if (rad12.checked == true) {
                d2 = 0;
            };
            if (rad13.checked == true) {
                d3 = 0;
            };
            if (rad14.checked == true) {
                d4 = 0;
            };
            if (rad15.checked == true) {
                d5 = 0;
            };
            if (rad16.checked == true) {
                d6 = 0;
            };
            if (rad17.checked == true) {
                d7 = 0;
            };
            if (rad18.checked == true) {
                d8 = 0;
            };
            if (rad19.checked == true) {
                d9 = 0;
            };
            if (rad20.checked == true) {
                d10 = 0;
            };
            if (rad21.checked == true) {
                d1 = 99;
            };
            if (rad22.checked == true) {
                d2 = 99;
            };
            if (rad23.checked == true) {
                d3 = 99;
            };
            if (rad24.checked == true) {
                d4 = 99;
            };
            if (rad25.checked == true) {
                d5 = 99;
            };
            if (rad26.checked == true) {
                d6 = 99;
            };
            if (rad27.checked == true) {
                d7 = 99;
            };
            if (rad28.checked == true) {
                d8 = 99;
            };
            if (rad29.checked == true) {
                d9 = 99;
            };
            if (rad30.checked == true) {
                d10 = 99;
            };

            $.post('/process_dat', {
                    d1: d1,
                    d2: d2,
                    d3: d3,
                    d4: d4,
                    d5: d5,
                    d6: d6,
                    d7: d7,
                    d8: d8,
                    d9: d9,
                    d10: d10,
                    age_val: age_val,
                    sex_val: sex_val,
                    socioeconomic_val: socioeconomic_val,
                    charttype_val: charttype_val,
                    matrixtype_val: matrixtype_val
                },
                function(result) {

                    const myList2 = [];
                    const case_number = [];
                    var k;


                    case_number.push(result.Second_response[10]);
                    console.log(case_number);
                    for (k = 0; k < 10; k++) {
                        myList2.push(result.Second_response[k]);
                    }
                    console.log(JSON.stringify(result))

                    textfunction(case_number);
                    activity(result.First_response);
                    updateBars2(myList2);
                });

        };
    };
    document.onreadystatechange = function() {

        var state = document.readyState;
        if (state == 'interactive') {

            makeVis_1();

        }
    };
</script>
<!--            </td>-->
<!--        </tr>-->
<!--    </table>-->
<div class="container2" id='vis-container2'></div>
<!--    <table id="tblTwo" style="width:50%; float:left">-->
<!--        <tr>-->
<!--            <td>-->
<script>
    //##########################Codes for Matrix
    var activity = function(data) {
        var dataset = data;
        var margin = {
                top: 90,
                right: 50,
                bottom: 0,
                left: 100
            },
            width = 320,
            height = 320;

        var x = d3.scale.ordinal().rangeBands([0, width]),
            z = d3.scale.linear().domain([0, 1000]).clamp(true),
            c = d3.scale.category10().domain(d3.range(10));

        //To prevent the chart from duplication by every update
        $("#vis-container2 svg").remove();
        $(".tooltip").remove();
        var tooltip = d3.select("body")
            .append("div")
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "white")
            .style("border", "solid")
            .style("border-width", "2px")
            .style("border-radius", "5px")
            .style("padding", "5px")
        var svg = d3.select("#vis-container2").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .style("margin-left", -margin.left + "px")
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        //Color legend for correlation matrix
        var colorlegend= d3.select("#vis-container2").append("svg")
            colorlegend.append("circle").attr("cx",10).attr("cy",10).attr("r", 6).style("fill", "#031281")
            colorlegend.append("text").attr("x", 20).attr("y", 11).text("Correlation greater than 0.2").style("font-size", "12px").attr("alignment-baseline","middle")
            colorlegend.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "#0785F5")
            colorlegend.append("text").attr("x", 20).attr("y", 31).text("Correlation between 0.1 and 0.2").style("font-size", "12px").attr("alignment-baseline","middle")
            colorlegend.append("circle").attr("cx",10).attr("cy",50).attr("r", 6).style("fill", "#16D1F7")
            colorlegend.append("text").attr("x", 20).attr("y", 51).text("Correlation between 0 and 0.1").style("font-size", "12px").attr("alignment-baseline","middle")
            colorlegend.append("circle").attr("cx",10).attr("cy",70).attr("r", 6).style("fill", "#FCDA09")
            colorlegend.append("text").attr("x", 20).attr("y", 71).text("Correlation between 0 and -0.1").style("font-size", "12px").attr("alignment-baseline","middle")
            colorlegend.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "#FCA709")
            colorlegend.append("text").attr("x", 20).attr("y", 91).text("Correlation between -0.1 and -0.2").style("font-size", "12px").attr("alignment-baseline","middle")
            colorlegend.append("circle").attr("cx",10).attr("cy",110).attr("r", 6).style("fill", "#F3510B")
            colorlegend.append("text").attr("x", 20).attr("y", 111).text("Correlation less than -0.2").style("font-size", "12px").attr("alignment-baseline","middle")

        //d3.json("Data-disease-matrix.json", function(miserables) {
        var matrix = [],
            nodes = dataset.nodes,
            n = nodes.length;

        // Compute index per node.
        nodes.forEach(function(node, i) {
            node.index = i;
            node.count = 0;
            matrix[i] = d3.range(n).map(function(j) {
                return {
                    x: j,
                    y: i,
                    z: 0
                };
            });
        });

        // Convert links to matrix; count character occurrences.

        dataset.links.forEach(function(link) {
            matrix[link.source][link.target].z += link.value;
            matrix[link.target][link.source].z += link.value;
            matrix[link.source][link.source].z = 1;
            matrix[link.target][link.target].z = 1;
            nodes[link.source].count += link.value;
            nodes[link.target].count += link.value;

        });

        // Precompute the orders.
        var orders = {
            name: d3.range(n).sort(function(a, b) {
                return d3.ascending(nodes[a].name, nodes[b].name);
            }),
            count: d3.range(n).sort(function(a, b) {
                return nodes[b].count - nodes[a].count;
            }),
            <!--                                group: d3.range(n).sort(function(a, b) { return nodes[b].group - nodes[a].group; })-->
        };

        // The default sort order.
        x.domain(orders.name);

        svg.append("rect")
            .attr("class", "background")
            .attr("width", width)
            .attr("height", height);

        var row = svg.selectAll(".row")
            .data(matrix)
            .enter().append("g")
            .attr("class", "row")
            .attr("transform", function(d, i) {
                return "translate(0," + x(i) + ")";
            })
            .each(row);

        row.append("line")
            .attr("x2", width);

        row.append("text")
            .attr("x", -6)
            .attr("y", x.rangeBand() / 2)
            .attr("dy", ".32em")
            .attr("text-anchor", "end")
            .text(function(d, i) {
                return nodes[i].name;
            });

        var column = svg.selectAll(".column")
            .data(matrix)
            .enter().append("g")
            .attr("class", "column")
            .attr("transform", function(d, i) {
                return "translate(" + x(i) + ")rotate(-90)";
            });

        column.append("line")
            .attr("x1", -width);

        column.append("text")
            .attr("x", 6)
            .attr("y", x.rangeBand() / 2)
            .attr("dy", ".32em")
            .attr("text-anchor", "start")
            .text(function(d, i) {
                return nodes[i].name;
            });

        function row(row) {
            var cell = d3.select(this).selectAll(".cell")
                .data(row.filter(function(d) {
                    return d.z;
                }))
                .enter().append("rect")
                .attr("class", "cell")
                .attr("x", function(d) {
                    return x(d.x);
                })
                .attr("width", x.rangeBand())
                .attr("height", x.rangeBand())
                <!--.style("fill-opacity", function(d) { return z(d.z*700); })-->
                <!--.style("fill", function(d) { return d.z<0 ? "red" : "black" })-->
                .style("fill", function(d) {
                    if (d.z == 3 || d.z == 1) {
                        return "black";
                    }
                    <!--                                          }if (d.z<0){-->
                    <!--                                          return "purple";}-->
                    <!--                                          else{-->
                    <!--                                          return "green";-->
                    <!--                                                }-->
                    //correlation rages for color intensity
                    if ( d.z >= 0 && d.z <= 0.1) {
                        return "#16D1F7";
                    }
                    if (0.1 < d.z && d.z < 0.2) {
                        return "#0785F5";
                    }
                    if (0.2 < d.z && d.z <= 1) {
                        return "#031281";
                    }

                    if (d.z >= (-0.1) && d.z < 0) {
                        return "#FCDA09";
                    }
                    if (d.z >= (-0.2) && d.z < (-0.1)) {
                        return "#FCA709";
                    }
                    if (d.z >= (-1) && d.z < (-0.2)) {
                        return "#F3510B";
                    }
                })
                <!--                                     .style("fill-opacity", function(d) { return( d.z>0 ? z(d.z*860) : z(d.z*700*(-2)));})-->

            <!--.style("fill", function(d) { return nodes[d.x].group == nodes[d.y].group ? c(nodes[d.x].group) : null; })-->

            .on("mouseover", function(d) {
                    //highlight text
                    d3.select(this).classed("cell-hover", true);
                    d3.selectAll(".rowLabel").classed("text-highlight", function(r, ri) {
                        return ri == (d.row - 1);
                    });
                    d3.selectAll(".colLabel").classed("text-highlight", function(c, ci) {
                        return ci == (d.col - 1);
                    });

                    //Update the tooltip position and value

                    if (d.z == "3") {

                        d3.select("#tooltip")
                            .style("left", (d3.event.pageX + 10) + "px")
                            .style("top", (d3.event.pageY - 10) + "px")
                            .select("#value")
                            .text("The correlation is undefined");
                        //Show the tooltip
                        d3.select("#tooltip").classed("hidden", false);

                    } else {
                        d3.select("#tooltip")
                            .style("left", (d3.event.pageX + 10) + "px")
                            .style("top", (d3.event.pageY - 10) + "px")
                            .select("#value")
                            .text('Correlation= ' + d.z);
                        //Show the tooltip
                        d3.select("#tooltip").classed("hidden", false);
                    };
                })
                .on("mouseout", function() {
                    d3.select(this).classed("cell-hover", false);
                    d3.selectAll(".rowLabel").classed("text-highlight", false);
                    d3.selectAll(".colLabel").classed("text-highlight", false);
                    d3.select("#tooltip").classed("hidden", true);
                });

        }

        d3.select("#order").on("change", function() {
            clearTimeout(timeout);
            order(this.value);
        });

        function order(value) {
            x.domain(orders[value]);

            var t = svg.transition().duration(2000);

            t.selectAll(".row")
                .delay(function(d, i) {
                    return x(i) * 4;
                })
                .attr("transform", function(d, i) {
                    return "translate(0," + x(i) + ")";
                })
                .selectAll(".cell")
                .delay(function(d) {
                    return x(d.x) * 4;
                })
                .attr("x", function(d) {
                    return x(d.x);
                });

            t.selectAll(".column")
                .delay(function(d, i) {
                    return x(i) * 4;
                })
                .attr("transform", function(d, i) {
                    return "translate(" + x(i) + ")rotate(-90)";
                });
        }

        var timeout = setTimeout(function() {
            order("count");
            d3.select("#order").property("selectedIndex", 2).node().focus();
        }, 5000);
        <!--});-->
    };

</script>
<!--            </td>-->
<!--        </tr>-->
<!--    </table>-->

<!--</div>-->

<table style="width:52%; ">

    <tr>
        <td>
            <div id='box1'>
                <input id="rad1" type="radio" name="probab1">
                <input id="rad2" type="radio" name="probab2">
                <input id="rad3" type="radio" name="probab3">
                <input id="rad4" type="radio" name="probab4">
                <input id="rad5" type="radio" name="probab5">
                <input id="rad6" type="radio" name="probab6">
                <input id="rad7" type="radio" name="probab7">
                <input id="rad8" type="radio" name="probab8">
                <input id="rad9" type="radio" name="probab9">
                <input id="rad10" type="radio" name="probab10"> &#10004;

            </div>
        </td>
    </tr>

    <tr>
        <td>
            <div id='box2'>
                <input id="rad11" type="radio" name="probab1">
                <input id="rad12" type="radio" name="probab2">
                <input id="rad13" type="radio" name="probab3">
                <input id="rad14" type="radio" name="probab4">
                <input id="rad15" type="radio" name="probab5">
                <input id="rad16" type="radio" name="probab6">
                <input id="rad17" type="radio" name="probab7">
                <input id="rad18" type="radio" name="probab8">
                <input id="rad19" type="radio" name="probab9">
                <input id="rad20" type="radio" name="probab10"> &#10006;

            </div>

        </td>
    </tr>

    <tr>
        <td>
            <div id='box3'>
                <input id="rad21" type="radio" name="probab1">
                <input id="rad22" type="radio" name="probab2">
                <input id="rad23" type="radio" name="probab3">
                <input id="rad24" type="radio" name="probab4">
                <input id="rad25" type="radio" name="probab5">
                <input id="rad26" type="radio" name="probab6">
                <input id="rad27" type="radio" name="probab7">
                <input id="rad28" type="radio" name="probab8">
                <input id="rad29" type="radio" name="probab9">
                <input id="rad30" type="radio" name="probab10"> &#10068;

            </div>
        </td>
    </tr>
</table>

<div id="tooltip" class="hidden">
    <p><span id="value"></span></p>
</div>

<MyBody class="ocks-org"></MyBody>

</html>
