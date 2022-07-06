var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var notes = parseFloat(lines.shift());
var x, y, z;

x = notes;
notes = notes * 100;
z = notes;

console.log("NOTAS:");
console.log(`${Math.floor(x / 100)} nota(s) de R$ 100.00`);
y = x % 100;
console.log(`${Math.floor(y / 50)} nota(s) de R$ 50.00`);
y = y % 50;
console.log(`${Math.floor(y / 20)} nota(s) de R$ 20.00`);
y = y % 20;
console.log(`${Math.floor(y / 10)} nota(s) de R$ 10.00`);
y = y % 10;
console.log(`${Math.floor(y / 5)} nota(s) de R$ 5.00`);
y = y % 5;
console.log(`${Math.floor(y / 2)} nota(s) de R$ 2.00`);
y = y % 2;
console.log("MOEDAS:");
console.log(`${Math.floor(y / 1)} moeda(s) de R$ 1.00`);
z = z % 100;
console.log(`${Math.floor(z / 50)} moeda(s) de R$ 0.50`);
z = z % 50;
console.log(`${Math.floor(z / 25)} moeda(s) de R$ 0.25`);
z = z % 25;
console.log(`${Math.floor(z / 10)} moeda(s) de R$ 0.10`);
z = z % 10;
console.log(`${Math.floor(z / 5)} moeda(s) de R$ 0.05`);
z = z % 5;
console.log(`${Math.floor(z / 1)} moeda(s) de R$ 0.01`);

