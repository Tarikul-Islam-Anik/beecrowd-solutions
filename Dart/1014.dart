import 'dart:io';

void main() {
  int x = int.parse(stdin.readLineSync());
  double y = double.parse(stdin.readLineSync());
  double consumption = x / y;
  print("${consumption.toStringAsFixed(3)} km/l");
}
