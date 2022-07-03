import 'dart:io';

void main() {
  int seconds = int.parse(stdin.readLineSync());
  int hours = seconds ~/ 3600;
  seconds = seconds % 3600;
  int minutes = seconds ~/ 60;
  seconds = seconds % 60;
  print("$hours:$minutes:$seconds");
}
