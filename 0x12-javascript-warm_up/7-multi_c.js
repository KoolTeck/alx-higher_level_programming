#!/usr/bin/node
const argv = process.argv;
const rep = parseInt(argv[2]);
if (isNaN(rep)) {
  console.log('Missing number of occurrences');
} else if (rep >= 0) {
  for (let i = 0; i < rep; i++) {
    console.log('C is fun');
  }
}
