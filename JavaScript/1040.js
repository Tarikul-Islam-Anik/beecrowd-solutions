var input = require("fs").readFileSync("/dev/stdin", "utf8");

var lines = input.split("\n");

var [n1, n2, n3, n4] = lines.shift().split(" ");

var n5 = parseFloat(lines.shift());

var avg =
  (parseFloat(n1) * 2 +
    parseFloat(n2) * 3 +
    parseFloat(n3) * 4 +
    parseFloat(n4)) /
  10;

console.log(`Media: ${avg.toFixed(1)}`);

if (avg >= 7) {
  console.log("Aluno aprovado.");
} else if (avg >= 5) {
  console.log("Aluno em exame.");
  console.log("Nota do exame: " + n5.toFixed(1));
  console.log("Aluno aprovado.");
  console.log("Media final: " + ((avg + n5)/2).toFixed(1));
} else if (avg < 5) {
  console.log("Aluno reprovado.");
}
