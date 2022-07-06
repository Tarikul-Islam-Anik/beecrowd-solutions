var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let a = parseFloat(lines.shift());
let b = parseFloat(lines.shift());
let c = parseFloat(lines.shift());

console.log("MEDIA = " + ((a * 2 + b * 3 + c * 5) / 10).toFixed(1));
