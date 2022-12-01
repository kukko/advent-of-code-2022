const { readFileSync } = require('fs');
const lines = readFileSync('input.txt', 'utf-8').split('\r\n');
const elves = [0];
for (let i = 0; i < lines.length; i++) {
  if (lines[i] == '') {
    elves[elves.length] = 0;
    continue;
  }
  elves[elves.length - 1] += parseInt(lines[i]);
}
let maxIndex = 0;
for (let i = 1; i < elves.length; i++) {
  if (elves[i] > elves[maxIndex]) {
    maxIndex = i;
  }
}
const elfNumber = maxIndex + 1;
let output = 'The ' + elfNumber;
switch (elfNumber.toString().substring(elfNumber.length - 1)) {
  case '1':
    output += 'st';
    break;
  case '2':
    output += 'nd';
    break;
  case '3':
    output += 'rd';
    break;
  default:
    output += 'th';
    break;
}
output += ' elf carries the most calories, which is ' + elves[maxIndex] + ' calorie.';
console.log(output);