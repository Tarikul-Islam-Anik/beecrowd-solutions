import 'dart:io';

void main() {
  int notes = int.parse(stdin.readLineSync());
  int hundred, fifty, twenty, ten, five, two, one;
  print(notes);
  hundred = notes ~/ 100;
  notes = notes % 100;
  fifty = notes ~/ 50;
  notes = notes % 50;
  twenty = notes ~/ 20;
  notes = notes % 20;
  ten = notes ~/ 10;
  notes = notes % 10;
  five = notes ~/ 5;
  notes = notes % 5;
  two = notes ~/ 2;
  notes = notes % 2;
  one = notes ~/ 1;
  print("${hundred} nota(s) de R\$ 100,00");
  print("${fifty} nota(s) de R\$ 50,00");
  print("${twenty} nota(s) de R\$ 20,00");
  print("${ten} nota(s) de R\$ 10,00");
  print("${five} nota(s) de R\$ 5,00");
  print("${two} nota(s) de R\$ 2,00");
  print("${one} nota(s) de R\$ 1,00");
}
