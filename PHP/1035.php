<?php
$x = rtrim(fgets(STDIN));
$a = explode(" ", $x)[0];
$b = explode(" ", $x)[1];
$c = explode(" ", $x)[2];
$d = explode(" ", $x)[3];
if ($b > $c && $d > $a && ($c + $d) > ($a + $b) && $c > 0 && $d > 0 && $a % 2 == 0) {
    echo "Valores aceitos\n";
} else {
    echo "Valores nao aceitos\n";
}
