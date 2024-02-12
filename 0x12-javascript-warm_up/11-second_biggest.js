#!/usr/bin/node

const myList = process.argv;

if (myList.length <= 3) { // If the list empty of have 1 number
  console.log(0);
} else {
  let bigest = myList[2]; // First number
  let secBig = myList[3]; // Second number

  for (let i = 2; i < myList.length; i++) {
    if (myList[i] > bigest) {
      secBig = bigest;
      bigest = myList[i];
    } else if (myList[i] > secBig && myList[i] < bigest) {
      secBig = myList[i];
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
// } else { // slice the list to have only the numbers and sort it [1, 2, `3`, 4]
//     const subList = process.argv.slice(2, lenList).sort((a, b) => a - b);
//     console.log(subList[subList.length - 2]) // Second elemnt from last
// }
