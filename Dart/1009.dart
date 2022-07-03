import 'dart:io';

void main() {
  String name = stdin.readLineSync();
  double salary = double.parse(stdin.readLineSync());
  double sales = double.parse(stdin.readLineSync());
  if (sales < 0) {
    print(salary);
  } else {
    double bonus = sales * 0.15;
    double total = salary + bonus;
    print("TOTAL = R\$ " + total.toStringAsFixed(2));
  }
}
