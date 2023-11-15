#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
if (isNaN(a)) {
  console.log('NaN');
} else {
  function add (a, b) {
    return a + b;
  }
  console.log(add(a, b));
}
