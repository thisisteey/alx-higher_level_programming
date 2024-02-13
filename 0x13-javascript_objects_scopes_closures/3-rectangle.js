#!/usr/bin/node
/*
Script that writes a class Rectangle that defines a rectangle
constructor must take 2 arguments w and h
the instance attribute width and height will be intialized with w and h respectively
create an empty object if w or h is equal to 0 or less than 0
prints the rectangle with the 'X' character
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let rect = '';
      for (let y = 0; y < this.width; y++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
