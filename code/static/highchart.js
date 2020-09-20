
const xCord = lowTemps;
const yCord = highTemps;
const coords = xCord.map((el, index)=> [el, yCord[index]]);

var chartFB = coords;
var chartCol = Precip;


Highcharts.chart('figure1', {

    credits: {
        enabled: false
    },

    chart: {
        type: 'columnrange',
        inverted: false
    },

    accessibility: {
        description: 'Image'
    },

    title: {
        text: 'Average High & Low Temperatures by Month'
    },

    xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },

    yAxis: {
        title: {
            text: 'Temperature ( °F )'
        }
    },

    tooltip: {
        valueSuffix: '°F'
    },

    plotOptions: {
        columnrange: {
            dataLabels: {
                enabled: true,
                format: '{y}°F'
            }
        }
    },

    legend: {
        enabled: false
    },

    series: [{
        name: 'Temperature Range',
        color: '#B22222',
        data: chartFB
    }]

});

Highcharts.chart('figure2', {
    
    credits: {
        enabled: false
    },
    
    chart: {
        type: 'column'
    },
    title: {
        text: 'Monthly Average Precipitation'
    },
    
    xAxis: {
        categories: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Precipitation (in)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} in</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },

    legend: {
        enabled: false
    },

    series: [{
        name: 'Amount',
        data: chartCol
    }]
});