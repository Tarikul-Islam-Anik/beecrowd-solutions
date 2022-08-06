var input = require("fs").readFileSync("/dev/stdin", "utf8");

var lines = input.split(" ");
var item = parseInt(lines[0]);
var qty = parseInt(lines[1]);

var menu = {
  1: 4.0,
  2: 4.5,
  3: 5.0,
  4: 2.0,
  5: 1.5,
};

console.log("Total: R$", (menu[item] * qty).toFixed(2));
