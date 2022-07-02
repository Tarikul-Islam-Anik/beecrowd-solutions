import 'dart:io';

void main() {
  double x = double.parse(stdin.readLineSync());
  double y = double.parse(stdin.readLineSync());
  x = x * 3.5;
  y = y * 7.5;
  double media = (x + y) / 11;
  print("MEDIA = " + media.toStringAsFixed(5));
}
