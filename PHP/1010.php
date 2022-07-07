<?php
$a = rtrim(fgets(STDIN));
$b = rtrim(fgets(STDIN));
echo "VALOR A PAGAR: R$ " . number_format((explode(" ", $a)[1] * explode(" ", $a)[2]) + (explode(" ", $b)[1] * explode(" ", $b)[2]), 2, '.', ''). PHP_EOL;
