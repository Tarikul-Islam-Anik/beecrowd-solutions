var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var x = lines.shift();
var y = lines.shift();

var x1 = parseFloat(x.split(" ")[0]);
var y1 = parseFloat(x.split(" ")[1]);

var x2 = parseFloat(y.split(" ")[0]);
var y2 = parseFloat(y.split(" ")[1]);

console.log(
  Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)).toFixed(4)
);
