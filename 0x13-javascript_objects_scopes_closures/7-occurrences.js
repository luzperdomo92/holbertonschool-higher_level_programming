#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOcurre = 0;
  let item;

  for (item of list) {
    if (item === searchElement) {
      numOcurre++;
    }
  }
  return numOcurre;
};
