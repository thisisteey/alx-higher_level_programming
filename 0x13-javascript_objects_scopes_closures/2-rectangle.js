#!/usr/bin/node
/*
Script that writes a class Rectangle that defines a rectangle
constructor must take 2 arguments w and h
the instance attribute width and height will be intialized with w and h respectively
create an empty object if w or h is equal to 0 or less than 0
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
