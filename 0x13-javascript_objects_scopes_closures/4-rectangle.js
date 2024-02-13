#!/usr/bin/node
// A class rectangle with the dimensions width and height
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints the rectangle with the 'X' character
  print () {
    for (let x = 0; x < this.height; x++) {
      let rect = '';
      for (let y = 0; y < this.width; y++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }

  // Exchnages the width and the height of the rectangle
  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  // Multiplies the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
