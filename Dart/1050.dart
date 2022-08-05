import 'dart:io';

void main() {
  var ddd = <int, String>{
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte",
  };

  int n = int.parse(stdin.readLineSync());

  if (n.toString().length == 2) {
    if (ddd.containsKey(n)) {
      print(ddd[n]);
    } else {
      print("DDD nao cadastrado");
    }
  } else {
    print("DDD invalido");
  }
}
