#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/// ///////////* This is my code *////////////////
myObject.incr = function () { myObject.value++; };
/// //////////////////////////////////////////////
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
