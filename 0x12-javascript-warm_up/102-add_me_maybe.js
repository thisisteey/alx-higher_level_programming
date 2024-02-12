#!/usr/bin/node
module.exports = {
  addMeMaybe: function (number, theFunction) {
    number++;
    theFunction(number);
  }
};
// Script that increments and calls a function using the prototype function (number, theFunction)
