import 'dart:io';

void main() {
  int count = 0;
  for (int i = 0; i < 5; i++) {
    int x = int.parse(stdin.readLineSync());
    if (x % 2 == 0) {
      count++;
    }
  }
  print("$count valores pares");
}
