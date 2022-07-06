var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split(" ");

var a = parseFloat(lines.shift());
var b = parseFloat(lines.shift());
var c = parseFloat(lines.shift());

var delta = b * b - 4 * a * c;
if (delta < 0 || a === 0) {
  console.log("Impossivel calcular");
} else {
  x1 = (-b + Math.sqrt(delta)) / (2 * a);
  x2 = (-b - Math.sqrt(delta)) / (2 * a);
  console.log("R1 =", x1.toFixed(5));
  console.log("R2 =", x2.toFixed(5));
}
