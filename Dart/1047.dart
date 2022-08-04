import 'dart:io';

void main() {
  var n = stdin.readLineSync().split(' ').map(int.parse).toList();
  if (n[2] > n[0]) {
    if (n[3] > n[1]) {
      print("O JOGO DUROU ${n[2] - n[0]} HORA(S) E ${n[3] - n[1]} MINUTO(S)");
    } else {
      print(
          "O JOGO DUROU ${n[2] - n[0] - 1} HORA(S) E ${60 + n[3] - n[1]} MINUTO(S)");
    }
  } else if (n[2] == n[0]) {
    if (n[3] > n[1]) {
      print("O JOGO DUROU ${n[2] - n[0]} HORA(S) E ${n[3] - n[1]} MINUTO(S)");
    } else if (n[3] == n[1]) {
      print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)");
    } else {
      print("O JOGO DUROU 23 HORA(S) E ${60 + n[3] - n[1]} MINUTO(S)");
    }
  }
}
