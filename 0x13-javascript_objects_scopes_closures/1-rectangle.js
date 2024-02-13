#!/usr/bin/node
/*
Script that writes a class Rectangle that defines a rectangle
constructor must take 2 arguments w and h
the instance attribute width and height will be intialized with w and h respectively
*/
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
