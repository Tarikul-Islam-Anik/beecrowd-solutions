<?php
$sec = rtrim(fgets(STDIN));
$hours = floor($sec / 3600);
$sec = fmod($sec, 3600);
$minutes = floor($sec / 60);
$sec = fmod($sec, 60);
echo $hours . ":" . $minutes . ":" . $sec . "\n";
