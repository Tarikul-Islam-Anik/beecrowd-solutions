import 'dart:io';

void main() {
  var input = stdin.readLineSync();
  int a = int.parse(input.split((' '))[0]);
  int b = int.parse(input.split((' '))[1]);

  if (a % b == 0 || b % a == 0) {
    print('Sao Multiplos');
  } else {
    print('Nao sao Multiplos');
  }
}
