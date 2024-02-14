#!/usr/bin/node

const myD = require('./101-data').dict;

newDict = {};
// Create a new dictionary:
//      A key is a number of occurrences
//      A value is the list of user ids

for (const num in myD) { 
  // For each old key in old dictionary
  // if the the value of the new key not exist or undefiend
  // make for this key a new value with type of list
  if (!newDict[myD[num]]) { newDict[myD[num]] = []; }

  newDict[myD[num]].push(num); // push at key the values in list
}
console.log(newDict);
