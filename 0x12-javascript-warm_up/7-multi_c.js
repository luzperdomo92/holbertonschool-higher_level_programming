#!/usr/bin/node
let iter;

if (process.argv[2]) {
  for (iter = 0; iter < parseInt(process.argv[2]); iter++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
