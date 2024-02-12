#!/usr/bin/node
const digs = Number.parseInt(process.argv[2]);
console.log(Number.isNaN(digs) ? 'Not a number' : 'My number: ' + digs);
/*
 Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
 */
