#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    for (let iter = 0; iter < this.width; iter++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
