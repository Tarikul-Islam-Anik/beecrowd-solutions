<?php
$x = rtrim(fgets(STDIN));
$y = rtrim(fgets(STDIN));
echo number_format($x / $y, 3, ".", '') . " km/l\n";
