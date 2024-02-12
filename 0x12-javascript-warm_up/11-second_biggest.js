#!/usr/bin/node
const ags = process.argv
  .slice(2)
  .map(ag => Number.parseInt(ag))
  .sort((x, y) => y - x);
const big2 = ags.length < 2 ? 0 : ags[1];
console.log(big2);
// Script that searches the second biggest integer in the list of arguments
