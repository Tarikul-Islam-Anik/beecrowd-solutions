import 'dart:io';

void main() {
  int x = int.parse(stdin.readLineSync());
  int y = int.parse(stdin.readLineSync());
  print(((y / 12) * x).toStringAsFixed(3));
}
