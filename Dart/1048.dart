import 'dart:io';

void main() {
  double salary = double.parse(stdin.readLineSync());
  double new_salary, readjusted_salary;
  int percentage;

  if ((salary >= 0) && (salary <= 400.00)) {
    new_salary = salary * 1.15;
    readjusted_salary = new_salary - salary;
    percentage = 15;
  } else if ((400.01 <= salary) && (salary <= 800.00)) {
    new_salary = salary * 1.12;
    readjusted_salary = new_salary - salary;
    percentage = 12;
  } else if ((800.01 <= salary) && (salary <= 1200.00)) {
    new_salary = salary * 1.10;
    readjusted_salary = new_salary - salary;
    percentage = 10;
  } else if ((1200.01 <= salary) && (salary <= 2000.00)) {
    new_salary = salary * 1.07;
    readjusted_salary = new_salary - salary;
    percentage = 7;
  } else {
    new_salary = salary * 1.04;
    readjusted_salary = new_salary - salary;
    percentage = 4;
  }

  print("Novo salario: ${new_salary.toStringAsFixed(2)}");
  print("Reajuste ganho: ${readjusted_salary.toStringAsFixed(2)}");
  print("Em percentual: $percentage %");
}
