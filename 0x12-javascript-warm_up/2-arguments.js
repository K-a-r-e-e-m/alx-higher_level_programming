#!/usr/bin/node
const myLen = process.argv.length;

if (myLen === 3) {
  console.log('Argument found');
} else if (myLen > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
