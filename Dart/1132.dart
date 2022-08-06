import 'dart:io';

void main() {
  int x = int.parse(stdin.readLineSync());
  int y = int.parse(stdin.readLineSync());
  if (x > y) {
    int temp = y;
    y = x;
    x = temp;
  }
  int s = 0;
  for (x; x <= y; x++) {
    if (x % 13 != 0) {
      s += x;
    }
  }
  print(s);
}
