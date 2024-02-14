#!/usr/bin/node

// This function prints the number of arguments already printed and the new argument value.
let num = 0;
exports.logMe = function (item) {
  console.log(`${num++}: ${item}`);
};
