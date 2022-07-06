var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var hours = parseInt(lines.shift());
var kilos = parseInt(lines.shift());

console.log(((kilos / 12) * hours).toFixed(3));
