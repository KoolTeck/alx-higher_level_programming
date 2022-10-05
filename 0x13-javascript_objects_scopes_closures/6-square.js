#!/usr/bin/node
const bSquare = require('./5-square');
module.exports = class Square extends bSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c || 'X');
      }
      process.stdout.write('\n');
    }
  }
};
