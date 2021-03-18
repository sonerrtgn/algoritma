<?php

$dosya = fopen('problem8.txt', 'r');
$icerik = fread($dosya, filesize('problem8.txt'));
$count  = 0;
$carpim = 0;
echo $icerik[49];
echo "<br>";
$gecici_carpim = 1;
    while($count <1000){
        if($icerik[$count+12] !=""){
            for($i = 0;$i<13;$i++){
            $gecici_carpim = $gecici_carpim * ((int)$icerik[$count+$i]);
            }            
            if($gecici_carpim > $carpim){
                $carpim = $gecici_carpim;
            }
            $gecici_carpim = 0;
            $count++;
        }else{
            echo "bir satır bitti";
            $count = $count +13;
        }
    }
echo $carpim;

?>
