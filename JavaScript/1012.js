var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split(" ");

a = parseFloat(lines[0]);
b = parseFloat(lines[1]);
c = parseFloat(lines[2]);

console.log("TRIANGULO: " + ((a * c) / 2).toFixed(3));
console.log("CIRCULO: " + (3.14159 * (c * c)).toFixed(3));
console.log("TRAPEZIO: " + (((a + b) * c) / 2).toFixed(3));
console.log("QUADRADO: " + (b * b).toFixed(3));
console.log("RETANGULO: " + (a * b).toFixed(3));
