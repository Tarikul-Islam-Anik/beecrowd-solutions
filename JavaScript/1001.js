var input = require("fs").readFileSync("/dev/stdin", "utf8");

var x = input.split("\n");

var A = parseInt(x.shift());
var B = parseInt(x.shift());

var sum = A + B;

console.log("X = " + sum);
