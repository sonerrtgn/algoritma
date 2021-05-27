"""

problem -> https://projecteuler.net/problem=63

Bizden basamak sayisi ve ustun ayni oldugu sayilardan kac tane oldugunu bulmamiz isteniyor.
bir sayidan sonra kac tane uste bakilacagimiz bilinmiyor.
hangi sayilarin ustune bakmamiz gerektigide bilinmiyor.
sorudu bu iki problem cozulurse bundan sonra soruyu cozmek kolaylasacaktir.
ilk olarka ilk probleme odaklanalim ve nereye kadar bakacagimizi bulmaya calisalim.
2^1 = 2 | basamak sayisi = 1, ust = 1  istedigimiz sayi, bakmaya devam edelim
2^2 = 4 | basamak sayisi = 1, ust = 2  istedigimiz sayi degil, bakmaya devam edelim
2^3 = 8 | basamak sayisi = 1, ust = 3
2^4 = 16 | basamak sayisi = 2, ust = 4
2^5 = 32 | basamak sayisi = 2, ust = 5
2^6 = 64 | basamak sayisi = 2, ust = 6
2^7 = 128 | basamak sayisi = 3, ust = 7
ilk bakista basamak sayisina gore ustun cok hizli ilerledigi gorunuyor basit bir kodla 500.uste kadar basamak sayisiile ust'un esit olmadigibi saptadim.
simdi biraz daha buyuk bir sayiya bakalim.
7^1 =  7      | bs = 1 ust = 1
7^2 =  49     | bs = 2 ust = 2
7^3 =  343    | bs = 3 ust = 3
7^4 =  2401   | bs = 4 ust = 4
7^5 =  16807  | bs = 5 ust = 5
7^6 =  117649 | bs = 6 ust = 6
7^7 =  823543 | bs = 6 ust = 7
7^8 =  5764801| bs = 7 ust = 8
burada da ilk olarak ayni sekilde hizlaniyor gibiler ancak biraz buyudukce ust daha hizli yukseliyor gibi ilk cikarimimiz ust bs'den buyuk olursa durak noktamizi bulmus olabilriz.
simdi hangi sayiya kadar bakacagimiza bakalim bunun icin ilk 10 uzerinden deneyelim.

10^1 = 10     | bs=2 ust =1
10^2 = 100    | bs=3 ust =2
10^3 = 1000   | bs=4 ust =3
10^4 = 10000  | bs=5 ust =4
10^5 = 100000 | bs=6 ust =5
burada da basamak sayisinin ustten daha hizli yukseldigi goruluyor.
yani demekki 10 ve daha buyuk sayilara bakmaya gerek yok demektir, cunku basamak sayisi 10da bile ust'ten hep bir fazla oluyorsa daha buyuk sayilarda bs sayisi hep daha buyuk olur.

calisma suresi yazdirma islemi kaldirilirsa ortalama: 0.001 saniye civarindadir, hiz acisindan oldukca performansli.


"""

import time
def bs_sayi(sayi):
    return len(str(sayi))

bas = time.time()
taban = 1
us = 1
adet_sayi = 0
while(taban < 10):
    if(us == bs_sayi(taban**us)):
        adet_sayi +=1
        print("taban:",taban,"ust:",us,"sonuc: ",taban**us)
    if(us> bs_sayi(taban**us)):
        #sayet us bssayidan daha buyukse artik diger sayilara bakailiriz yukarida 10dan kucuk sayilar icin ust'un daha hizli ilerledigibi saptamistik.
        taban+=1
        us = 0
    us+=1
print("Kacn tane basamak sayisi ile ustu ayni sayi vardir: ",adet_sayi)
son = time.time()
print("Calisma suresi: ",(son-bas))
