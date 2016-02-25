$(document).ready(function(){
    
    // Get all of the list names and status
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
            skiruns.push( "<li id='" + i + "'>" + val.run + " - " + val['run--status'] + "</li>" );
        });

        $( "<ul/>", {
            "class": "ski-runs",
            html: skiruns.join( "" )
        }).appendTo( $("[rel=js-runs]") );

    });
    
});