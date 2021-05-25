var chart;
var chart2;
//한국 시간으로 세팅
Highcharts.setOptions({
    global:{
        useUTC :false
    }
})

function requestData() {
    $.ajax({
        //데이터 받아오는 부분
        url: '/live-data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 40;

            //첫번째 데이터 받아오기
            chart.series[0].addPoint(point[0], true, shift);

            var series2 = chart.series[1],
                shift = series2.data.length > 40;

            // 두번째 데이터 받아오기
            chart.series[1].addPoint(point[1], true, shift);


            // call it again after 8초
            setTimeout(requestData, 8000);
        },
        cache: false
    });
}


function requestData2() {
    $.ajax({
        //데이터 받아오는 부분
        url: '/live-data2',
        success: function(point) {
            //첫번째 데이터 받아오기
            var series = chart2.series[0],
                shift = series.data.length > 20;

            chart2.series[0].addPoint(point[0], true, shift);
            // 두번째 데이터 받아오기
            var series2 = chart2.series[1],
                shift = series2.data.length > 20;

            chart2.series[1].addPoint(point[1], true, shift);

            // 세번째 데이터 받아오기
            var series3 = chart2.series[2],
                shift = series3.data.length > 20;
            
            chart2.series[2].addPoint(point[2], true, shift);
            // 네번째 데이터 받아오기
            var series4 = chart2.series[3],
                shift = series4.data.length > 20;
            
            chart2.series[3].addPoint(point[3], true, shift);
            // 다섯번째 데이터 받아오기
            var series5 = chart2.series[4],
                shift = series5.data.length > 20;
            
            chart2.series[4].addPoint(point[4], true, shift);
            // 여섯째 데이터 받아오기
            var series6 = chart2.series[5],
                shift = series6.data.length > 20;
            
            chart2.series[5].addPoint(point[5], true, shift);


            // call it again after 8초
            setTimeout(requestData2, 8000);
        },
        cache: false
    });
}


$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'People statistic'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },
        series: [{
            name: 'Man',
            data: []
            },{
            name: 'Woman',
            data:[]
        }]
    });

    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container2',
            type: 'column',
            events: {
                load: requestData2
            }
        },
        title: {
            text: '광고별 관심도'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
            // categories: ['Clothes', 'Devices','Perfume'],
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'rate by advertisement(%)',
                margin: 80
            }
        },

        tooltip: {
            formatter: function () {
              return '<b>' + this.x + '</b><br/>' +
                this.series.name + ': ' + this.y + '<br/>' +
                'Total: ' + this.point.stackTotal;
            }
        },

        plotOptions: {
            column: {
              stacking: 'normal'
            }
        },

        series: [{
            name: 'Clothes_man',
            data: [],
            stack: 'Clothes'
            },{
            name: 'Clothes_woman',
            data: [],
            stack: 'Clothes'
            },{
            name: 'Devices_man',
            data:[],
            stack: 'Devices'
            },{
            name: 'Devices_woman',
            data: [],
            stack: 'Devices'
            },{
            name: 'Perfume_man',
            data:[],
            stack: 'Perfume'
            },{
            name: 'Perfume_woman',
            data: [],
            stack: 'Perfume'
            },]
    });
});