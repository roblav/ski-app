var express = require('express');
var app = express();
var fs = require('fs');

app.use('/', express.static(__dirname + '/public'));

app.get('/', function (req, res) {
    res.render('index');
});

app.get('/skiconditions/:date', function (req, res) {

    var file = __dirname + '/database/' + req.params.date + '.json';

    fs.readFile(file, {encoding: 'utf8'}, function(error, data) {
        if (error) {
            return console.error(error.message);
        }
        res.send(data);
    });
});

app.listen(3000, function () {
    console.log('BOB Example app listening on port 3000!');
});