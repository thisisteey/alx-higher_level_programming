#!/usr/bin/node
const dict = require('./101-data.js').dict;
const nDict = {};
Object.getOwnPropertyNames(dict).forEach(numOcc => {
  if (nDict[dict[numOcc]] === undefined) {
    nDict[dict[numOcc]] = [numOcc];
  } else {
    nDict[dict[numOcc]].push(numOcc);
  }
});
console.log(nDict);
// Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
// Script must import dict from the file 101-data.js and print the new dictionary at the end
// In the new dictionary: a key is a number of occurrences and a value is the list of user ids
