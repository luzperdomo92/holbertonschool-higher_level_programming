#!/usr/bin/node
let iter;
const size = process.argv[2];

if (process.argv[2]) {
  if (isNaN(size) === false) {
    for (iter = 0; iter < parseInt(size); iter++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
