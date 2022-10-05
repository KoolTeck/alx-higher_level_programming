#!/usr/bin/node
const argv = process.argv;
const len = argv.length;
const args = [];
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    args.push(parseInt(argv[i]));
  }
  args.sort((a, b) => {
    return b - a;
  });
  console.log(args[1]);
}
