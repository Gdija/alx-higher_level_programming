#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const datas = JSON.parse(body);
  const result = {};
  for (const data of datas) {
    if (data.completed) {
      if (!result[data.userId]) {
        result[data.userId] = 1;
      } else {
        result[data.userId]++;
      }
    }
  }
  console.log(result);
});
