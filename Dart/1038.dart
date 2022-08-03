import 'dart:io';

void main() {
  var items = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
  };
  var order = stdin.readLineSync();
  var orderList = order.split(' ');
  var total = items[int.parse(orderList[0])] * int.parse(orderList[1]);
  print("Total: R\$ " + total.toStringAsFixed(2));
}
