import 'dart:io';
import 'dart:math';

void main() {
  String input1 = stdin.readLineSync();
  String input2 = stdin.readLineSync();
  List x, y;
  x = input1.split(" ");
  y = input2.split(" ");
  x = x.map((e) => double.parse(e)).toList();
  y = y.map((e) => double.parse(e)).toList();
  print(
      sqrt((pow((y[1] - x[1]), 2) + pow((x[0] - y[0]), 2))).toStringAsFixed(4));
}
