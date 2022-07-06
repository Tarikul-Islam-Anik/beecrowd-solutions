var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var x = lines.shift();
var y = lines.shift();

x = x.split(" ");
y = y.split(" ");

console.log("VALOR A PAGAR: R$ " + (x[1] * x[2] + y[1] * y[2]).toFixed(2));
