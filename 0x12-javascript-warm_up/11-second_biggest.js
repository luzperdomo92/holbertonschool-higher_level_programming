#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let max;
  let second;

  for (let iter = 2; iter < process.argv.length; iter++) {
    const arg = parseInt(process.argv[iter]);
    if (max === undefined || arg > max) {
      second = max;
      max = arg;
    } else if (second === undefined || arg > second) {
      second = arg;
    }
  }
  console.log(second);
}
