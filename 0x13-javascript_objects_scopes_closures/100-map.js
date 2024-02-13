#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((element, idx) => element * idx));
// Script that imports an array and computes a new array
// Script must import list from the file 100-data.js and must use map
// A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
// Print both the initial list and the new list
