import 'dart:io';

void main() {
  int n = int.parse(stdin.readLineSync());
  for (int i = 0; i < n; i++) {
    List r = stdin.readLineSync().split(' ');
    int r1 = int.parse(r[0]);
    int r2 = int.parse(r[1]);
    print(r1 + r2);
  }
}
