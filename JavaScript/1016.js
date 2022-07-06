var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

console.log(parseFloat(lines.shift()) * 2, "minutos");
