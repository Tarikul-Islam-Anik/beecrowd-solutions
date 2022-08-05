import 'dart:io';

void main() {
  var n = stdin.readLineSync().split(' ').map(int.parse).toList();
  int h1, h2, m1, m2, hour_difference, minute_difference;
  h1 = n[0];
  m1 = n[1];
  h2 = n[2];
  m2 = n[3];
  if ((h2 > h1) || ((h2 == h1) && (m2 > m1))) {
    hour_difference = h2 - h1;
  } else {
    hour_difference = (h2 - h1) + 24;
  }
  if (m2 < m1) {
    hour_difference -= 1;
    minute_difference = (m2 - m1) + 60;
  } else {
    minute_difference = m2 - m1;
  }
  print("O JOGO DUROU $hour_difference HORA(S) E $minute_difference MINUTO(S)");
}
