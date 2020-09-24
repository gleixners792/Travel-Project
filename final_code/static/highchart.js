

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

    // subtitle: {
    //     text: 'Cleveland, Ohio'
    // },

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
        // data: [
        //     [21.7, 34.4],
        //     [23.6, 37.5],
        //     [30.2, 46.6],
        //     [40.4, 59.1],
        //     [50.1, 69.5],
        //     [59.8, 78.6],
        //     [64.3, 82.6],
        //     [63.1, 80.8],
        //     [56.0, 73.9],
        //     [45.4, 62.3],
        //     [36.9, 50.8],
        //     [26.4, 38.3]
        // ]
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
        //data: [2.72, 2.34, 2.93, 3.49, 3.66, 3.43, 3.46, 3.51, 3.81, 3.07, 3.62, 3.10]
    }]
});