#!/usr/bin/node
const argv = process.argv;
const istInt = parseInt(argv[2]);
const secInt = parseInt(argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(istInt, secInt);
