#!/usr/bin/node

function fact(num) { return (num === 0 ? 1 : num * fact(num - 1)) }
console.log(fact(Number(process.argv[2])));

// Another solution with loop
// let fact = 1;
// for (let i = Number(process.argv[2]); i > 0; i--) { fact *= i; }
// console.log(fact);
