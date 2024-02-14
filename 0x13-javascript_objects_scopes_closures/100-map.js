#!/usr/bin/node

let myList = require('./100-data');
console.log(myList.list); // Before map

const newList = myList.list.map((value, index) => value * index);

console.log(newList); // After map
