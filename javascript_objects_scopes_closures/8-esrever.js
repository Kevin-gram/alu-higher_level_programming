#!/usr/bin/node
exports.esrever = function (list) {
  const reverseLst = [];
  while (list.length > 0) {
    reverseLst.push(list.pop());
  }
  return reverseLst;
};
