#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(process.argv[3], body);
  }
});
