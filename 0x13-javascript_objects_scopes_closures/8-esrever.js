#!/usr/bin/node
// A function that returns the reversed version of a list without using the built-in method reverse
// Prototype: exports.esrever = function (list)
exports.esrever = function (list) {
  const lent = list.length;
  const revArr = new Array(lent);
  list.forEach((element, idx) => {
    revArr[lent - idx - 1] = element;
  });
  return revArr;
};
