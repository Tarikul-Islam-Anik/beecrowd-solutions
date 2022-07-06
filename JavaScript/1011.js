var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var r = parseInt(lines.shift());

console.log("VOLUME =", ((3.14159 * (r * r * r) * 4) / 3).toFixed(3));
