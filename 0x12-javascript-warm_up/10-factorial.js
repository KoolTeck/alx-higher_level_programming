#!/usr/bin/node
const argv = process.argv;
const arg = parseInt(argv[2]);
function factorial (n) {
  if (isNaN(n) || n == 0) {
    return 1;
  }
  if (n < 0) {
    return -1;
  }
  return n * factorial(n - 1);
}
const val = factorial(arg);
console.log(val);
