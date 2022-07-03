import 'dart:io';

void main() {
  int num = int.parse(stdin.readLineSync());
  int salary = int.parse(stdin.readLineSync());
  double bonus = double.parse(stdin.readLineSync());
  double total = salary * bonus;

  print("NUMBER = $num");
  print("SALARY = U\$ " + total.toStringAsFixed(2));
}
