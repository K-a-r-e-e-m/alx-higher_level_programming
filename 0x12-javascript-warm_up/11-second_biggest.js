#!/usr/bin/node

const myList = process.argv;

if (myList.length <= 3) { // If the list empty of have 1 number
  console.log(0);
} else {
  let bigest = Number(myList[2]); // First number
  let secBig = Number(myList[3]); // Second number

  for (let i = 2; i < myList.length; i++) {
    if (Number(myList[i]) > bigest) {
      secBig = bigest;
      bigest = Number(myList[i]);
    } else if (Number(myList[i]) > secBig && Number(myList[i]) < bigest) {
      secBig = Number(myList[i]);
    }
  }
  console.log(secBig);
}

// Another solution (Advanced)
//
// const myList = process.argv;
// const lenList = myList.length;
// if (myList.length <= 3) {
//     console.log(0);
// } else { // slice the list to have only the numbers and map Number funcoin and sort it
//     const subList = process.argv.slice(2, lenList).map(Number).sort((a, b) => a - b);
//     console.log(subList[subList.length - 2]) // Second elemnt from last
// }
