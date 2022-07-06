<?php
$a = rtrim(fgets(STDIN));
$b = rtrim(fgets(STDIN));
$c = rtrim(fgets(STDIN));
echo "MEDIA = ". number_format((float)((($a*2+$b*3+$c*5)/10)),1,".",'') . "\n";
?>