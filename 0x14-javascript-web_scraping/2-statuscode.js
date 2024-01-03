#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, data) {
  if (err) {
    return console.error(err);
  }
  console.log('code: ' + response.statusCode);
});
