#!/usr/bin/node
const fSys = require('fs');
const fstArgCtnts = fSys.readFileSync(process.argv[2]).toString();
const scdArgCtnts = fSys.readFileSync(process.argv[3]).toString();
fSys.writeFileSync(process.argv[4], fstArgCtnts + scdArgCtnts);
// Script that concats 2 files
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination
