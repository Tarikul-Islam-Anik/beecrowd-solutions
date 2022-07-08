import 'dart:io';

void main() {
  var n = stdin.readLineSync();
  var x, y;
  x = double.parse(n.split(' ')[0]);
  y = double.parse(n.split(' ')[1]);
  if ((x == 0.0) && (y == 0.0)) {
    print("Origem");
  } else if (x == 0.0) {
    print("Eixo Y");
  } else if (y == 0.0) {
    print("Eixo X");
  } else if ((x > 0.0) && (y > 0.0)) {
    print("Q1");
  } else if ((x < 0.0) && (y > 0.0)) {
    print("Q2");
  } else if ((x < 0.0) && (y < 0.0)) {
    print("Q3");
  } else if ((x > 0.0) && (y < 0.0)) {
    print("Q4");
  }
}
