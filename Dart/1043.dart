import 'dart:io';

void main() {
  var n = stdin.readLineSync().split(' ').map(double.parse).toList();
  if (n[0] + n[1] > n[2] && n[0] + n[2] > n[1] && n[1] + n[2] > n[0]) {
    print('Perimetro = ${n[0] + n[1] + n[2]}');
  } else {
    print('Area = ${(n[0] + n[1]) * n[2] / 2}');
  }
}
