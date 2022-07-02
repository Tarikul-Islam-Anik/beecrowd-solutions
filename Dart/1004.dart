import 'dart:io';

void main() {
  int x = int.parse(stdin.readLineSync());
  int y = int.parse(stdin.readLineSync());
  int prod = x * y;
  print("PROD = $prod");
}
