#!/usr/bin/node

// This function returns the reversed version of a list
// without using built-in method reverse
exports.esrever = function (list) {
  const revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
