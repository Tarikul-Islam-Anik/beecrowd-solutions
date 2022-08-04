import 'dart:io';

void main() {
  var n = stdin.readLineSync().split(' ').map(double.parse).toList();
  if (n[0] < n[1]) {
    var temp = n[0];
    n[0] = n[1];
    n[1] = temp;
  }
  if (n[0] < n[2]) {
    var temp = n[0];
    n[0] = n[2];
    n[2] = temp;
  }
  if (n[1] < n[2]) {
    var temp = n[1];
    n[1] = n[2];
    n[2] = temp;
  }
  if (n[0] >= n[1] + n[2]) {
    print("NAO FORMA TRIANGULO");
  } else if (n[0] * n[0] == n[1] * n[1] + n[2] * n[2]) {
    print("TRIANGULO RETANGULO");
  } else if (n[0] * n[0] > n[1] * n[1] + n[2] * n[2]) {
    print("TRIANGULO OBTUSANGULO");
  } else if (n[0] * n[0] < n[1] * n[1] + n[2] * n[2]) {
    print("TRIANGULO ACUTANGULO");
  }
  if (n[0] == n[1] && n[1] == n[2]) {
    print("TRIANGULO EQUILATERO");
  } else if (n[0] == n[1] || n[1] == n[2] || n[0] == n[2]) {
    print("TRIANGULO ISOSCELES");
  }
}
