var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var N = parseInt(lines.shift());
var hours = parseInt(lines.shift());
var percent = parseFloat(lines.shift());

console.log(`NUMBER = ${N}`);
console.log(`SALARY = U$ ${(hours * percent).toFixed(2)}`);
