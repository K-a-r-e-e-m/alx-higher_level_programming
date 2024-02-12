#!/usr/bin/node
console.log(Number(process.argv[2]) ? `My number: ${process.argv[2]}` : 'Not a number');

/* OR */
// if (Number(process.argv[2])) {
//   console.log('My number:', process.argv[2]);
// } else {
//   console.log('Not a number');
// }
