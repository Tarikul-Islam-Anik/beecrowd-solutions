<?php
$r = rtrim(fgets(STDIN));
echo "VOLUME = " . number_format((($r * $r * $r * 4 * 3.14159) / 3), 3, '.', '') . PHP_EOL;
