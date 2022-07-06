var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

var days = parseInt(lines.shift());

var years = Math.floor(days / 365);
var months = Math.floor((days % 365) / 30);
var days = Math.floor((days % 365) % 30);

console.log(`${years} ano(s)`);
console.log(`${months} mes(es)`);
console.log(`${days} dia(s)`);
