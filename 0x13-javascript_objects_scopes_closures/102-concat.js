#!/usr/bin/node

const fs = require('fs');

const file1 = fs.readFileSync('fileA', 'utf8');
const file2 = fs.readFileSync('fileB', 'utf8');

const combined = file1 + file2;

fs.writeFileSync('fileC', combined);
