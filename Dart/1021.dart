import 'dart:io';

void main() {
  double notes = double.parse(stdin.readLineSync());
  double x, y, z;
  x = notes;
  notes *= 100;
  z = notes;
  print("NOTAS:");
  print("${(x ~/ 100).toInt()} nota(s) de R\$ 100.00");
  y = x % 100;
  print("${(y ~/ 50).toInt()} nota(s) de R\$ 50.00");
  y = y % 50;
  print("${(y ~/ 20).toInt()} nota(s) de R\$ 20.00");
  y = y % 20;
  print("${(y ~/ 10).toInt()} nota(s) de R\$ 10.00");
  y = y % 10;
  print("${(y ~/ 5).toInt()} nota(s) de R\$ 5.00");
  y = y % 5;
  print("${(y ~/ 2).toInt()} nota(s) de R\$ 2.00");
  y = y % 2;
  print("MOEDAS:");
  print("${(y ~/ 1).toInt()} moeda(s) de R\$ 1.00");
  z = z % 100;
  print("${(z ~/ 50).toInt()} moeda(s) de R\$ 0.50");
  z = z % 50;
  print("${(z ~/ 25).toInt()} moeda(s) de R\$ 0.25");
  z = z % 25;
  print("${(z ~/ 10).toInt()} moeda(s) de R\$ 0.10");
  z = z % 10;
  print("${(z ~/ 5).toInt()} moeda(s) de R\$ 0.05");
  z = z % 5;
  print("${(z ~/ 1).toInt()} moeda(s) de R\$ 0.01");
}
