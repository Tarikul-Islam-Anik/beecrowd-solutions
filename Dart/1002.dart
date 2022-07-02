import 'dart:io';

void main() {
  double r = double.parse(stdin.readLineSync());
  double area = r * r * 3.14159;
  print("A=" + area.toStringAsFixed(4));
}
