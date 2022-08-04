import 'dart:io';

void main() {
  var n = stdin.readLineSync().split(' ').map(int.parse).toList();
  if (n[0] < n[1]) {
    print("O JOGO DUROU ${n[1] - n[0]} HORA(S)");
  } else if (n[0] > n[1]) {
    print("O JOGO DUROU ${n[1] + 24 - n[0]} HORA(S)");
  } else {
    print("O JOGO DUROU 24 HORA(S)");
  }
}
