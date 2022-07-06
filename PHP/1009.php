<?php
$name = rtrim(fgets(STDIN));
$salary = rtrim(fgets(STDIN));
$sales = rtrim(fgets(STDIN));

$percentage = $sales * 0.15;
$total = $salary + $percentage;

echo "TOTAL = R$ " . number_format($total, 2, ".", "") . PHP_EOL;
