import 'dart:io';

void main() {
  String inputs = stdin.readLineSync();
  List inputsList = inputs.split(" ");
  inputsList = inputsList.map((e) => int.parse(e)).toList();
  int a, b, c, d;
  a = inputsList[0];
  b = inputsList[1];
  c = inputsList[2];
  d = inputsList[3];
  if (b > c && d > a && (c + d) > (a + b) && c > 0 && d > 0 && a % 2 == 0) {
    print("Valores aceitos");
  } else {
    print("Valores nao aceitos");
  }
}
