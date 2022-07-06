var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var person_name = lines.shift();
var salary = parseFloat(lines.shift());
var sales = parseFloat(lines.shift());

if (sales > 0) {
  console.log("TOTAL = R$", (salary + sales * 0.15).toFixed(2));
} else {
  console.log("TOTAL = R$", salary.toFixed(2));
}