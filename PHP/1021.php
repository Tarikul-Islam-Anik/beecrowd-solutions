<?php
$notes = rtrim(fgets(STDIN));
$x = $notes;
$notes = $notes * 100;
$z = $notes;
echo "NOTAS:\n";
echo floor($x / 100) . " nota(s) de R$ 100.00\n";
$y = fmod($x, 100);
echo floor($y / 50) . " nota(s) de R$ 50.00\n";
$y = fmod($y, 50);
echo floor($y / 20) . " nota(s) de R$ 20.00\n";
$y = fmod($y, 20);
echo floor($y / 10) . " nota(s) de R$ 10.00\n";
$y = fmod($y, 10);
echo floor($y / 5) . " nota(s) de R$ 5.00\n";
$y = fmod($y, 5);
echo floor($y / 2) . " nota(s) de R$ 2.00\n";
$y = fmod($y, 2);
echo "MOEDAS:\n";
echo floor($y / 1) . " moeda(s) de R$ 1.00\n";
$z = fmod($z, 100);
echo floor($z / 50) . " moeda(s) de R$ 0.50\n";
$z = fmod($z, 50);
echo floor($z / 25) . " moeda(s) de R$ 0.25\n";
$z = fmod($z, 25);
echo floor($z / 10) . " moeda(s) de R$ 0.10\n";
$z = fmod($z, 10);
echo floor($z / 5) . " moeda(s) de R$ 0.05\n";
$z = fmod($z, 5);
echo floor($z / 1) . " moeda(s) de R$ 0.01\n";
