#!/usr/bin/node
const args = parseInt(process.argv[2]);
if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let x = 1; x <= args; x++) {
    let square = '';
    for (let y = 1; y <= args; y++) square += 'X';
    console.log(square);
  }
}
