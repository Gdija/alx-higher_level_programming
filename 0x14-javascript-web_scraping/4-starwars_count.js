#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const movie of results) {
    if (movie.characters.find(id => id.endsWith('18/'))) {
      count++;
    }
  }
  console.log(count);
});
