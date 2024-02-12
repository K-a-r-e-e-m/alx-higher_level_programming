#!/usr/bin/node
console.log(process.argv[2] ? process.argv[2] : 'No argument');

// Another solution
// if (process.argv[2]) {
//   console.log(process.argv[2]);
// } else {
//   console.log('No argument');
// }
