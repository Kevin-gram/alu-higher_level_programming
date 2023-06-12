#!/usr/bin/node
let nmbr = process.argv[2];
let  convert = parseInt(nmbr);
if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
