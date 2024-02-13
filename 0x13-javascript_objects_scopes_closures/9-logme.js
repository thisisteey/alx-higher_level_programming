#!/usr/bin/node
let logCounter = 0;
exports.logMe = function (item) {
  console.log(logCounter + ': ' + item);
  logCounter++;
};
// A function that prints the number of arguments already printed and the new argument value
// Prototype: exports.logMe = function (item)
// Output format: <number arguments already printed>: <current argument value>
