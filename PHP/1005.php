<?php
$a = rtrim(fgets(STDIN));
$b = rtrim(fgets(STDIN));
echo "MEDIA = ". number_format((float)((($a*3.5+$b*7.5)/11)),5,".",'') . "\n";
?>