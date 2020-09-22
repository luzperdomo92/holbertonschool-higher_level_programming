#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const myObject = {};
    const data = JSON.parse(body);
    data.forEach((completed) => {
      if (completed.completed === true) {
        const count = completed.userId;
        if (count in myObject) {
          myObject[count]++;
        } else {
          myObject[count] = 1;
        }
      }
    });
    console.log(myObject);
  }
});
