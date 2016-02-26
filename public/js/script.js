$(document).ready(function(){
    
    // Get all of the list names and status
    // Append these details to the page
    $.getJSON( "data/96suz4vm.json", function( data ) {

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
        var skiruns = [];
        $.each( data.results.mountainRuns, function( i, val ) {
            skiruns.push( "<li id='" + i + "'>" + val.run + "("+skiRunGrade(val.run)+")" +" - " + val['run--status'] + "</li>" );
        });

        $( "<ul/>", {
            "class": "ski-runs",
            html: skiruns.join( "" )
        }).appendTo( $("[rel=js-runs]") );

    });

    //Create a function to take in each ski run and return the ski run name plus the
    // grade of ski run

    function skiRunGrade(strSkiRun){
        var skiRunGrades = {
            'Half Pipe': 'Red',
            'Ptarmigan Bowl': 'Green',
            'Terrain Park': 'Green',
            'Ciste Fairway': 'Green',
            'Ciste Bowl': 'Green',
            'Traverse': 'Green',
            'Coire Cas': 'Green',
            'Cas Shred': 'Green',
            '105': 'Blue',
            'ZigZags': 'Green',
            'Gun Barrel': 'Blue',
            'Chicken Gully': 'Red',
            'Fiacaill Piste': 'Blue',
            'M1': 'Red',
            'M1 105 Link': 'Blue',
            'White Lady': 'Red',
            'Sheiling': 'Blue',
            'The Sheiling Shred': 'Blue',
            "Cottam's Way": 'Green',
            'Burnside': 'Green',
            'Home Road': 'Green',
            'Car Park': 'Green',
            'Fiacaill Ridge': 'Blue',
            'M2': 'Blue',
            'Ciste Gully': 'Red',
            'West Wall': 'Black',
            'Ryvoan': 'Red',
            'Aonach Bowl': 'Red',
            'East Wall No 1 Gully':	'Red',
            'East Wall No 2 Gully': 'Black',
            'Over Yonder': 'Blue',
            'Day Lodge': 'Blue'
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