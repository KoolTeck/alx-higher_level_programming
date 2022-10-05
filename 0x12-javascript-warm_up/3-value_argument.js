#!/usr/bin/node
const argv = process.argv;
let count = 0;
argv.forEach(val => {
  count++;
});
if (count === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
