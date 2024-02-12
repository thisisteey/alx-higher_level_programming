#!/usr/bin/node
function factorial (digs) {
  if (Number.isNaN(digs) || (digs <= 0)) {
    return 1;
  } else {
    return digs * factorial(digs - 1);
  }
}
console.log(factorial(Number.parseInt(process.argv[2])));
// Script that computes and prints a factorial
