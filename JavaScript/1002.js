var input = require("fs").readFileSync("/dev/stdin", "utf8");

let r = parseFloat(input);
console.log("A=" + (r * r * 3.14159).toFixed(4).toString());
