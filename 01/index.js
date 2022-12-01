const { readFileSync } = require('fs');
const lines = readFileSync('input.txt', 'utf-8').split('\r\n');
const elves = [0];

function getNumberPostfix(number) {
  switch (number.toString().substring(elfNumber.length - 1)) {
    case '1':
      return 'st';
    case '2':
      return 'nd';
    case '3':
      return 'rd';
    default:
      return 'th';
  }
}

for (let i = 0; i < lines.length; i++) {
  if (lines[i] == '') {
    elves[elves.length] = 0;
    continue;
  }
  elves[elves.length - 1] += parseInt(lines[i]);
}
const numberOfTopElves = 3;
let maxIndexes = [];
for (let i = 0; i < numberOfTopElves; i++) {
  maxIndexes.push(0);
}
for (let i = 1; i < elves.length; i++) {
  for (let j = maxIndexes.length - 1; j >= 0; j--) {
    if (elves[i] > elves[maxIndexes[j]]) {
      maxIndexes = [...(j > 0 ? maxIndexes.slice(1, j + 1) : []), i, ...(maxIndexes.slice(j + 1))];
      break;
    }
  }
}
const elfNumber = maxIndexes[maxIndexes.length - 1] + 1;
console.log('The ' + elfNumber + getNumberPostfix(elfNumber) + ' elf carries the most calories, which is ' + elves[maxIndexes[maxIndexes.length - 1]] + ' calorie.');
console.log('The top ' + maxIndexes.length + ' elves:');
let caloriesOfTopElves = 0;
for (let i = maxIndexes.length - 1; i >= 0; i--) {
  console.log('\t' + (maxIndexes.length - i) + '. The ' + (maxIndexes[i] + 1) + getNumberPostfix(maxIndexes[i] + 1) + ' with ' + elves[maxIndexes[i]] + ' calorie.')
  caloriesOfTopElves += elves[maxIndexes[i]];
}
console.log('They carry a total of ' + caloriesOfTopElves + ' calorie.');