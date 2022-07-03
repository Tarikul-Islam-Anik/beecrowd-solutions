import 'dart:io';

void main() {
  String inputs = stdin.readLineSync();
  List values = inputs.split(" ");
  double a = double.parse(values[0]);
  double b = double.parse(values[1]);
  double c = double.parse(values[2]);
  print("TRIANGULO: " + ((a * c) / 2).toStringAsFixed(3));
  print("CIRCULO: " + (3.14159 * (c * c)).toStringAsFixed(3));
  print("TRAPEZIO: " + ((a + b) * c / 2).toStringAsFixed(3));
  print("QUADRADO: " + (b * b).toStringAsFixed(3));
  print("RETANGULO: " + (a * b).toStringAsFixed(3));
}
