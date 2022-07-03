import 'dart:io';

void main() {
  String input1 = stdin.readLineSync();
  String input2 = stdin.readLineSync();
  int qty1 = int.parse(input1.split(' ')[1]);
  double price1 = double.parse(input1.split(' ')[2]);
  int qty2 = int.parse(input2.split(' ')[1]);
  double price2 = double.parse(input2.split(' ')[2]);
  double total = (qty1 * price1) + (qty2 * price2);
  print("VALOR A PAGAR: R\$ " + total.toStringAsFixed(2));
}
