var express = require('express');
var app = express();
var fs = require('fs');
var nunjucks = require('nunjucks');

app.use('/', express.static(__dirname + '/public'));

nunjucks.configure('public', {
    autoescape: true,
    watch: true,
    express: app
});

app.get('/index', function (req, res) {
    res.render('index.html');
});

app.get('/display-one-day', function (req, res) {
    res.render('display-one-day.html');
});

app.get('/test', function(req, res) {
    res.render('test.html', {
        title : 'My First Nunjucks Page',
        items : [
            { name : 'item #1' },
            { name : 'item #2' },
            { name : 'item #3' },
            { name : 'item #4' }
        ]
    });
});

app.get('/skiconditions/:date', function (req, res) {

    var file = __dirname + '/database/' + req.params.date + '.json';

    fs.readFile(file, {encoding: 'utf8'}, function(error, data) {
        if (error) {
            return console.error(error.message);
        }
        var json = JSON.parse(data);
        //From this data get the count for open and closed runs
        //open, opening, closed, on hold
        //return object for each run [Start to use TDD]

        res.render('ski-results.html', {"data":json, "view":data});
    });
});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});