<?php
$x = rtrim(fgets(STDIN));
$y = rtrim(fgets(STDIN));
echo number_format($x * $y/12, 3, ".", '') . "\n";
