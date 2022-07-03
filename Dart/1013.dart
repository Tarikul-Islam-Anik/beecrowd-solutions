import 'dart:io';

void main() {
  String inputs = stdin.readLineSync();
  List values = inputs.split(" ");
  List lst = values.map((e) => int.parse(e)).toList();
  int m = lst[0];

  for (int i = 0; i < lst.length; i++) {
    if (lst[i] > m) {
      m = lst[i];
    }
  }
  print(m.toString() + " eh o maior");
}
