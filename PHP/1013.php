<?php
$x = rtrim(fgets(STDIN));
$a = explode(' ', $x)[0];
$b = explode(' ', $x)[1];
$c = explode(' ', $x)[2];
$max = $a;
if ($b > $max) {
    $max = $b;
}

if ($c > $max) {
    $max = $c;
}

echo $max . " eh o maior" . PHP_EOL;
