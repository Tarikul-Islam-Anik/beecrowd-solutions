<?php
$num = rtrim(fgets(STDIN));
$hours = rtrim(fgets(STDIN));
$percent = rtrim(fgets(STDIN));
echo "NUMBER = ".($num) . "\n";
echo "SALARY = U$ ".(number_format($hours*$percent,2,".","")) . "\n";
?>