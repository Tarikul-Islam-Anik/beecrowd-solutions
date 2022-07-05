import 'dart:io';
import 'dart:math';

void main() {
  String inputs = stdin.readLineSync();
  List inputsList = inputs.split(" ");
  inputsList = inputsList.map((e) => double.parse(e)).toList();
  double a, b, c;
  a = inputsList[0];
  b = inputsList[1];
  c = inputsList[2];
  double delta = (b * b) - (4 * a * c);
  if ((delta < 0) || (a == 0)) {
    print("Impossivel calcular");
  } else {
    double x1 = (-b + sqrt(delta)) / (2 * a);
    double x2 = (-b - sqrt(delta)) / (2 * a);
    print("R1 = ${x1.toStringAsFixed(5)}");
    print("R2 = ${x2.toStringAsFixed(5)}");
  }
}
