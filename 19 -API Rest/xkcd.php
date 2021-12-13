<?php

echo file_get_contents('https://xkcd.com/info.0.json').PHP_EOL;

#Use php xkcd.php | jq to get better results

$json = file_get_contents('https://xkcd.com/info.0.json');
#To get data as an array
$data = json_decode($json, true);

echo $data['img'];