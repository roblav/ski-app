$(document).ready(function(){

    // Get all of the list names and status
    // Append these details to the page
    $.getJSON( "data/20160225.json", function( data ) {

        //Return all the ski lifts
        var skilifts = [];
        $.each( data.results.mountainLifts, function( i, val ) {
            skilifts.push( "<li id='" + i + "'>" + val.lift + " - " + val['lift--status'] + "</li>" );
        });

        $( "<ul/>", {
            "class": "ski-lifts",
            html: skilifts.join( "" )
        }).appendTo( $("[rel=js-lifts]") );

        //Return all the ski runs
        var skiruns = [],
            greenruns = [],
            blueruns = [],
            redruns = [],
            blackruns = [];

        $.each( data.results.mountainRuns, function( i, val ) {



            switch(skiRunGrade(val.run)){
                case 'green':
                    greenruns.push( "<li id='" + i + "'>" + val.run + "("+skiRunGrade(val.run)+")" +" - " + val['run--status'] + "</li>" );
                    break;
                case 'blue':
                    blueruns.push( "<li id='" + i + "'>" + val.run + "("+skiRunGrade(val.run)+")" +" - " + val['run--status'] + "</li>" );
                    break;
                case 'red':
                    redruns.push( "<li id='" + i + "'>" + val.run + "("+skiRunGrade(val.run)+")" +" - " + val['run--status'] + "</li>" );
                    break;
                case 'black':
                    blackruns.push( "<li id='" + i + "'>" + val.run + "("+skiRunGrade(val.run)+")" +" - " + val['run--status'] + "</li>" );
                    break;
                default:
                    break;
            }
            skiruns.push( "<li id='" + i + "'>" + val.run + "("+skiRunGrade(val.run)+")" +" - " + val['run--status'] + "</li>" );
        });

        $( "<ul/>", {
            "class": "greenruns",
            html: greenruns.join( "" )
        })
            .appendTo( $("[rel=js-greenruns]") );

        $( "<ul/>", {
            "class": "blueruns",
            html: blueruns.join( "" )
        })
            .appendTo( $("[rel=js-blueruns]") );

        $( "<ul/>", {
            "class": "redruns",
            html: redruns.join( "" )
        })
            .appendTo( $("[rel=js-redruns]") );

        $( "<ul/>", {
            "class": "blackruns",
            html: blackruns.join( "" )
        })
            .appendTo( $("[rel=js-blackruns]") );

    });

    //Create a function to take in each ski run and return the ski run name plus the
    // grade of ski run

    function skiRunGrade(strSkiRun){
        var skiRunGrades = {
            'Half Pipe': 'red',
            'Ptarmigan Bowl': 'green',
            'Terrain Park': 'green',
            'Ciste Fairway': 'green',
            'Ciste Bowl': 'green',
            'Traverse': 'green',
            'Coire Cas': 'green',
            'Cas Shred': 'green',
            '105': 'blue',
            'ZigZags': 'green',
            'Gun Barrel': 'blue',
            'Chicken Gully': 'red',
            'Fiacaill Piste': 'blue',
            'M1': 'red',
            'M1 105 Link': 'blue',
            'White Lady': 'red',
            'Sheiling': 'blue',
            'The Sheiling Shred': 'blue',
            "Cottam's Way": 'green',
            'Burnside': 'green',
            'Home Road': 'green',
            'Car Park': 'green',
            'Fiacaill Ridge': 'blue',
            'M2': 'blue',
            'Ciste Gully': 'red',
            'West Wall': 'black',
            'Ryvoan': 'red',
            'Aonach Bowl': 'red',
            'East Wall No 1 Gully':	'red',
            'East Wall No 2 Gully': 'black',
            'Over Yonder': 'blue',
            'Day Lodge': 'blue'
        };

        //For each value of strSkiRun, compare it to the key and when matched return the value

        for (var prop in skiRunGrades) {
            if(prop === strSkiRun){
                return skiRunGrades[prop];
            }
        }

    }

    skiRunGrade();

});