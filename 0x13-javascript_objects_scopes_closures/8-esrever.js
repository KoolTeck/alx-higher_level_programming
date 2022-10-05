#!/usr/bin/node
exports.esrever = function (list) {
  const esrever = [];
  let len = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    esrever[i] = list[len--];
  }
  return esrever;
};
