<?php
$a = rtrim(fgets(STDIN));
$b = rtrim(fgets(STDIN));
$x1 = explode(" ", $a)[0];
$x2 = explode(" ", $b)[0];
$y1 = explode(" ", $a)[1];
$y2 = explode(" ", $b)[1];

echo number_format(sqrt(pow($x2 - $x1, 2) + pow($y2 - $y1, 2)), 4, ".", '') . "\n";
