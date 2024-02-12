#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const ntimes = Number(process.argv[2]);
  let x = 0;
  while (x < ntimes) {
    console.log('X'.repeat(ntimes));
    x++;
  }
}
// Script that prints a square using the X character
