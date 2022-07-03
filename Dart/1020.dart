import 'dart:io';

void main() {
  int days = int.parse(stdin.readLineSync());
  int years = days ~/ 365;
  days = days % 365;
  int months = days ~/ 30;
  days = days % 30;

  print("$years ano(s)");
  print("$months mes(es)");
  print("$days dia(s)");
}
