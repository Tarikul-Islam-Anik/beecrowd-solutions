var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var notes = parseInt(lines.shift());

var hundred, fifty, twenty, ten, five, two, one;
console.log(notes);
hundred = Math.floor(notes / 100);
notes = notes % 100;
console.log(hundred, "nota(s) de R$ 100,00");
fifty = Math.floor(notes / 50);
notes = notes % 50;
console.log(fifty, "nota(s) de R$ 50,00");
twenty = Math.floor(notes / 20);
notes = notes % 20;
console.log(twenty, "nota(s) de R$ 20,00");
ten = Math.floor(notes / 10);
notes = notes % 10;
console.log(ten, "nota(s) de R$ 10,00");
five = Math.floor(notes / 5);
notes = notes % 5;
console.log(five, "nota(s) de R$ 5,00");
two = Math.floor(notes / 2);
notes = notes % 2;
console.log(two, "nota(s) de R$ 2,00");
one = notes;
console.log(one, "nota(s) de R$ 1,00");
