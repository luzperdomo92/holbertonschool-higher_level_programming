#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let iter;
    for (iter = 0; iter < this.height; iter++) { console.log('X'.repeat(this.width)); }
  }
}
module.exports = Rectangle;
