import 'dart:io';

void main() {
  var input = stdin.readLineSync();
  var n1 = int.parse(input.split(' ')[0]);
  var n2 = int.parse(input.split(' ')[1]);
  var n3 = int.parse(input.split(' ')[2]);
  if ((n1 - n2) == 0) {
    print("S");
  } else if ((n1 - n3) == 0) {
    print("S");
  } else if ((n2 - n3) == 0) {
    print("S");
  } else if (((n1 + n2) - n3) == 0) {
    print("S");
  } else if (((n1 + n3) - n2) == 0) {
    print("S");
  } else if (((n2 + n3) - n1) == 0) {
    print("S");
  } else {
    print("N");
  }
}
