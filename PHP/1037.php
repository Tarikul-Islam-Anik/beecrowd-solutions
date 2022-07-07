<?php
$x = rtrim(fgets(STDIN));
if ($x >= 0 && $x <= 25) {
    echo "Intervalo [0,25]" . PHP_EOL;
} else if ($x > 25 && $x <= 50) {
    echo "Intervalo (25,50]" . PHP_EOL;
} else if ($x > 50 && $x <= 75) {
    echo "Intervalo (50,75]" . PHP_EOL;
} else if ($x > 75 && $x <= 100) {
    echo "Intervalo (75,100]" . PHP_EOL;
} else {
    echo "Fora de intervalo" . PHP_EOL;
}
