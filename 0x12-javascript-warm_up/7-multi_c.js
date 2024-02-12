#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let t = 0;
  while (t < x) {
    console.log('C is fun');
    t++;
  }
}
// Script that prints x times “C is fun”
