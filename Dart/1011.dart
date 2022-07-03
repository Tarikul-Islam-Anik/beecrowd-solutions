import 'dart:io';

void main() {
  int r = int.parse(stdin.readLineSync());
  print("VOLUME = " + ((4.0 / 3) * 3.14159 * (r * r * r)).toStringAsFixed(3));
}
