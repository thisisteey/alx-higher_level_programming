#!/usr/bin/node
function add (a, b) {
  return a + b;
}
console.log(add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3])));
// Script that prints the addition of 2 integers using this function add(a, b)
