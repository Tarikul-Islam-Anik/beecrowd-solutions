<?php
$days = rtrim(fgets(STDIN));
$years = floor($days / 365);
$days = fmod($days, 365);
$months = floor($days / 30);
$days = fmod($days, 30);
echo $years . " ano(s)\n";
echo $months . " mes(es)\n";
echo $days . " dia(s)\n";
