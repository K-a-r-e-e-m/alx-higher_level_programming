#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
// In const
// We can not change the whole object but we can change their attribute
// and the object still the same object
