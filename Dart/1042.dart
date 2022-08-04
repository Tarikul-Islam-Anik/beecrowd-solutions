import 'dart:io';

void main() {
  var n = stdin.readLineSync().split(' ').map(int.parse).toList();
  var list = [];
  for (var i = 0; i < n.length; i++) {
    list.add(n[i]);
  }
  n.sort();
  for (var i = 0; i < n.length; i++) {
    print(n[i]);
  }
  print("");
  for (var i = 0; i < n.length; i++) {
    print(list[i]);
  }
}
