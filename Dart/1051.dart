import 'dart:io';

void main() {
  double salary = double.parse(stdin.readLineSync());

  if (salary <= 2000) {
    print("Isento");
  } else if (salary > 2000 && salary <= 3000) {
    print("R\$ ${((salary - 2000) * 0.08).toStringAsFixed(2)}");
  } else if (salary > 3000 && salary <= 4500) {
    print("R\$ ${((salary - 3000) * 0.18 + (1000 * 0.08)).toStringAsFixed(2)}");
  } else if (salary > 4500) {
    print(
        "R\$ ${((salary - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)).toStringAsFixed(2)}");
  }
}
