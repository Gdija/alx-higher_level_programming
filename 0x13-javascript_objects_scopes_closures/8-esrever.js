#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  for (let i = list.length; i > 0; i--) {
    array.push(list[i - 1]);
  }
  return array;
};
