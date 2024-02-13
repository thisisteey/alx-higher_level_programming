#!/usr/bin/node
const SquareAncestor = require('./5-square');
// A class Square that defines a square and inherits from Square of 5-square.js
class Square extends SquareAncestor {
  charPrint (c) {
    const prntchar = c === undefined ? 'X' : c;
    const horizln = new Array(this.width).fill(prntchar, 0, this.width);
    const grdrows = new Array(this.height).fill(horizln.join(''), 0, this.height);
    console.log(grdrows.join('\n'));
  }
}
module.exports = Square;
// An instance method called charPrint(c) is created that prints the rectangle using the character c
// If c is undefined, use the character X
