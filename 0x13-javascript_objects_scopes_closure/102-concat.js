#!/usr/bin/node
const fs = require('fs');

const alphaArg = fs.readFileSync(process.argv[2]).toString();
const betaArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], alphaArg + betaArg);
