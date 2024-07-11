$(document).ready(function(){
    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8080/consulta",
        data: {},
        dataType: "json",
        success: function (json) {
            console.log(json);

            //Carlos Herrera Tello
            let templateCH = `
            <p class="follows">Followers en Twitter: `+ json["1"].seguidores_T +`</p>
            <p class="follows">Favoritos en Twitter: `+ json["1"].favoritos_T+`</p>
            <p class="follows">Total de likes en Fb: `+ json["1"].likes_F +`</p>
            <p class="follows">Total de seguidores en Fb: `+ json["1"].seguidores_F +`</p>
            `;
            $("#datosCH").html(templateCH);
        
            //Raúl Morón
            let templateRM = `
            <p class="follows">Followers en Twitter: `+ json["2"].seguidores_T +`</p>
            <p class="follows">Favoritos en Twitter: `+ json["2"].favoritos_T+`</p>
            <p class="follows">Total de likes en Fb: `+ json["2"].likes_F +`</p>
            <p class="follows">Total de seguidores en Fb: `+ json["2"].seguidores_F +`</p>
            `;
            $("#datosRM").html(templateRM);
        
            //Juan mora
            let templateJM = `
            <p class="follows">Followers en Twitter: `+ json["3"].seguidores_T +`</p>
            <p class="follows">Favoritos en Twitter: `+ json["3"].favoritos_T+`</p>
            <p class="follows">Total de likes en Fb: `+ json["3"].likes_F +`</p>
            <p class="follows">Total de seguidores en Fb: `+ json["3"].seguidores_F +`</p>
            `;
            $("#datosJM").html(templateJM);
        
            //Graphics
            google.charts.load('current', {'packages':['corechart']});
            
            /* Historial */
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
                let templateGraphics = ``;
            
                let graficaPuntajes = [
                    ['Día', 'Carlos Herrera', 'Raúl Morón', 'Juan Magaña'],
                ];
            
                let longitud = json["1"]["puntajes"].length;
                for (let i = 0; i < longitud; i++) {
                    let col = [
                        json["1"]["puntajes"][i]['fecha-hora'], 
                        json["1"]["puntajes"][i]['puntaje'], 
                        json["2"]["puntajes"][i]['puntaje'], 
                        json["3"]["puntajes"][i]['puntaje']
                    ];
                    graficaPuntajes.push(col);
                }
            
                var data = google.visualization.arrayToDataTable(graficaPuntajes);
                
                var options = {
                    title: 'Presencia en redes sociales',
                    curveType: 'function',
                    legend: { position: 'bottom' },
                    series: {
                        0: { color: '#FFC300' },
                        1: { color: '#C70039' },
                        2: { color: '#0eb62f' },
                        }
                };
                var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
                chart.draw(data, options);
            }

            /* Barras */
            google.charts.setOnLoadCallback(drawBarras);
            function drawBarras() {
                var data = google.visualization.arrayToDataTable([
                ["Element", "Density", { role: "style" } ],
                ["Carlos Herrera", (json["1"].seguidores_T + json["1"].favoritos_T + json["1"].likes_F + json["1"].seguidores_F), "#FFC300"],
                ["Raúl Morón", (json["2"].seguidores_T + json["2"].favoritos_T + json["2"].likes_F + json["2"].seguidores_F), "#C70039 "],
                ["Juan Magaña", (json["3"].seguidores_T + json["3"].favoritos_T + json["3"].likes_F + json["3"].seguidores_F), "#0eb62f"]
                ]);
                
                var view = new google.visualization.DataView(data);
                view.setColumns([0, 1,
                    { calc: "stringify",
                        sourceColumn: 1,
                        type: "string",
                        role: "annotation" },
                    2]);
            
                var optionsBarras = {
                    title: "Cantidad de personas que los siguen",
                    height: 500,
                    bar: {groupWidth: "95%"},
                    legend: { position: "none" },
                };
                var chartBarras = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
                chartBarras.draw(view, optionsBarras);
            }
        
            $(window).resize(function(){
                drawChart();
                drawBarras();
            });
        }
    });

    $('#btnRecoleccion').click(function (e) { 
        e.preventDefault();
        $('#btnRecoleccion').attr("disabled", true);
        $('#btnRecoleccion').text('Recolectando Datos');
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8080/recoleccion/api-webScraping",
            data: {},
            dataType: "json",
            success: function (response) {
                console.log(response);
                alert('Recoleccion de datos terminado, recarge la pagina')
            }
        });
    });
});
