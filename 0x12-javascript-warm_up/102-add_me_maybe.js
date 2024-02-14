#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number += 1); // OR (++number)
};
