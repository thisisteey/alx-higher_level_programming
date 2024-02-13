#!/usr/bin/node
exports.converter = function (base) {
  return function (digToConv) {
    return digToConv.toString(base);
  };
};
// A function that converts a number from base 10 to another base passed as argument
// Prototype: exports.converter = function (base)
