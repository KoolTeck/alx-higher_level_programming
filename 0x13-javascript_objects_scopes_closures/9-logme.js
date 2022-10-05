#!/usr/bin/node
exports.logMe = function (item) {
  console.log(`${counter++}: ${item}`);
};
let counter = 0;
