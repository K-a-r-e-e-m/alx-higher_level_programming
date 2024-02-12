#!/usr/bin/node

if (!Number(process.argv[2])) { console.log('Missing number of occurrences'); }
const myStr = 'C is fun';
for (let i = 0; i < process.argv[2]; i++) { console.log(myStr); }
