#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      nbOccurences++;
    }
  });
  return nbOccurences;
};
