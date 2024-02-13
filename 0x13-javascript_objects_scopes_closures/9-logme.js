#!/usr/bin/node

let logCounter = 0;

exports.logMe = function (item) {
  console.log(`${logCounter}: ${item}`); // Adjust logCounter to start from 0\
  logCounter++;
};
