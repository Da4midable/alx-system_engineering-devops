#!/usr/bin/node

exports.esrever = function (list) {
  const reverseIt = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseIt.push(list[i]);
  }
  return reverseIt;
};
