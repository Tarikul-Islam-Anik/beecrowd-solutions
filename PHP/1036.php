<?php
$x = rtrim(fgets(STDIN));
$a = explode(" ", $x)[0];
$b = explode(" ", $x)[1];
$c = explode(" ", $x)[2];
$delta = $b * $b - 4 * $a * $c;
if (($delta < 0) || ($a == 0)) {
    echo "Impossivel calcular" . "\n";
} else {
    $x1 = (-$b + sqrt($delta)) / (2 * $a);
    $x2 = (-$b - sqrt($delta)) / (2 * $a);
    echo "R1 = " . number_format($x1, 5, '.', '') . "\n";
    echo "R2 = " . number_format($x2, 5, '.', '') . "\n";
}
