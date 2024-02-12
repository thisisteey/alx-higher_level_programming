#!/usr/bin/node
module.exports = {
  callMeMoby: function (x, theFunction) {
    for (let t = 0; t < x; t++) {
      theFunction();
    }
  }
};
// Script that executes x times a function using the prototype function (x, theFunction)
