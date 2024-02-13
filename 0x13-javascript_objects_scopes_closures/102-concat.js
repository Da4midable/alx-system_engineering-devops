#!/usr/bin/node

const fs = require('fs');

const file1 = fs.readFileSync('fileA', 'utf8');
const file2 = fs.readFileSync('fileB', 'utf8');

const combined = file1 + '\n' + file2 + '\n';

fs.writeFileSync('fileC', combined);
