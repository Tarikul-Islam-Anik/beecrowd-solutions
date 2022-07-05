import 'dart:io';

void main() {
  double x = double.parse(stdin.readLineSync());
  if (x >= 0 && x <= 25) {
    print("Intervalo [0,25]");
  } else if (x > 25 && x <= 50) {
    print("Intervalo (25,50]");
  } else if (x > 50 && x <= 75) {
    print("Intervalo (50,75]");
  } else if (x > 75 && x <= 100) {
    print("Intervalo (75,100]");
  } else {
    print("Fora de intervalo");
  }
}
