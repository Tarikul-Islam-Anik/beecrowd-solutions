<?php
$r = rtrim(fgets(STDIN));
echo "A=" . number_format((float) (($r * $r * 3.14159)), 4, '.', '') . "\n";
?>