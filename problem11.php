<?php
$dosya = fopen('problem11.txt', 'r');
$icerik = fread($dosya, filesize('problem11.txt'));
$dizi = array();
$count = 0;
$a = 0;
$b = 1;

for($i = 0; $i<20; $i++){
    for($j=0; $j<20; $j++){
        $dizi[$i][$j] = ($icerik[$a+$count*3])*10+$icerik[$b+$count*3];
        $count++;
    }
    $a++;
    $b++;
}

$carpim = 1;
for($i = 0; $i<20; $i++){
    for($j=0; $j<20; $j++){
        // sol toplama
        if($j+3 <= 19){
            if($carpim < $dizi[$i][$j]*$dizi[$i][$j+1]*$dizi[$i][$j+2]*$dizi[$i][$j+3]){
                $carpim = $dizi[$i][$j]*$dizi[$i][$j+1]*$dizi[$i][$j+2]*$dizi[$i][$j+3];
                echo $dizi[$i][$j];
                echo "-";
                echo $dizi[$i][$j+1];
                echo "-";
                echo $dizi[$i][$j+2];
                echo "-";
                echo $dizi[$i][$j+3];
                echo "-";
                echo "<br>";
            }
        }
        //asagi carpma
        if($i+3 <=19){
            if($carpim < $dizi[$i][$j]*$dizi[$i+1][$j]*$dizi[$i+2][$j]*$dizi[$i+3][$j]){
                $carpim = $dizi[$i][$j]*$dizi[$i+1][$j]*$dizi[$i+2][$j]*$dizi[$i+3][$j];
                echo $dizi[$i][$j];
                echo "-";
                echo $dizi[$i+1][$j];
                echo "-";
                echo $dizi[$i+2][$j];
                echo "-";
                echo $dizi[$i+3][$j];
                echo "-";
                echo "<br>";

            }
        }
        //sag-asagi carpim
        if($i+3 <= 19 && $j+3 <=19){
            if($carpim <  $dizi[$i][$j]*$dizi[$i+1][$j+1]*$dizi[$i+2][$j+2]*$dizi[$i+3][$j+3]){
                $carpim =  $dizi[$i][$j]*$dizi[$i+1][$j+1]*$dizi[$i+2][$j+2]*$dizi[$i+3][$j+3];
                echo $dizi[$i][$j];
                echo "-";
                echo $dizi[$i+1][$j+1];
                echo "-";
                echo $dizi[$i+2][$j+2];
                echo "-";
                echo $dizi[$i+3][$j+3];
                echo "-";
                echo "<br>";
            }
        }
    }   
}
echo $carpim;



?>
