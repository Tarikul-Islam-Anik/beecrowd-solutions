var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split(" ");

var a = parseInt(lines[0]);
var b = parseInt(lines[1]);
var c = parseInt(lines[2]);

var max = a;

if (b > max) max = b;
if (c > max) max = c;

console.log(max, "eh o maior");
