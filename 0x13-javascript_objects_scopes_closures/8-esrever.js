#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let iter;
  for (iter = list.length - 1; iter >= 0; iter--) {
    newList.push(list[iter]);
  }
  return (newList);
};
