<?php
$input = rtrim(fgets(STDIN));
$a = explode(' ', $input)[0];
$b = explode(' ', $input)[1];
$c = explode(' ', $input)[2];
echo "TRIANGULO: " . number_format((($a * $c) / 2), 3, '.', '') . PHP_EOL;
echo "CIRCULO: " . number_format((($c * $c) * 3.14159), 3, '.', '') . PHP_EOL;
echo "TRAPEZIO: " . number_format((($a + $b) * $c / 2), 3, '.', '') . PHP_EOL;
echo "QUADRADO: " . number_format(($b * $b), 3, '.', '') . PHP_EOL;
echo "RETANGULO: " . number_format(($a * $b), 3, '.', '') . PHP_EOL;
