#!/usr/bin/node

const cSquare = require('./5-square');

class Square extends cSquare {
  // This method prints the rectangle using the character c
  // and If c is undefined, use the character X
  charPrint (c) {
    if (!c) { c = 'X'; }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
    // Another Solution for previous for loop
    //
    // for (let i = 0; i < this.height; i++) {
    //   let myRow = '';
    //   for (let j = 0; j < this.width; j++) {
    //     myRow += c;
    //   }
    //   console.log(myRow);
    // }
  }
}
module.exports = Square;
