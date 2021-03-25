"""
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49


3 5 7 , 13 17 21 , 31 37 43 sol üst köşelerdeki sayılar isteniyor.
alt köşenin sayılar n*n olduğu için asal olmazlar hiçbir zaman, 7x7 sprialdeki köşegen sayısı 13, asal olanların sayısı ise
8- bu oran yaklaşık 13/8 'dir(%60) bizden hani aXa 'da bu oranın %60 altına düşeceği soruluyor.
koşegenlerin en büyüğü n*n , diğerleri ise sırasıyla (n*n)-(n-1),(n*n)-2*(n-1),(n*n)-3*(n-1) n*n asal olmadığını bildiğimiz
için geri kalan 3 durum bizim için önemlidir sprial her büyüdüğünde baktığımız köşe sayısı 4 artmalıdır.

"""
import math
def asalmi(x):
    if(x%2 == 0 and x!=2):
        return 0
    if(x<0):
        return 0
    bs = 3
    dk = int(math.sqrt(x))+1
    while(bs < dk):
        if(x%bs == 0):
            return 0
        bs+=2
    return 1
def sprial_sayi_ver(x):
    dizi = []
    dizi.append((x*x)-(x-1))
    dizi.append((x*x)-2*(x-1))
    dizi.append((x*x)-3*(x-1))
    return dizi

sprial_sayisi = 5
asal_sayisi = 3
kose_sayisi = 5 #3x3 sprial alınarak_baslaniyor.
asal_sayi_orani = int((100/kose_sayisi))*asal_sayisi
while(asal_sayi_orani > 10):
    yeni_sayilar = sprial_sayi_ver(sprial_sayisi)
    if(asalmi(yeni_sayilar[0]) == 1):
        asal_sayisi+=1
    if(asalmi(yeni_sayilar[1]) == 1):
        asal_sayisi+=1
    if(asalmi(yeni_sayilar[2]) == 1):
        asal_sayisi+=1
        
    kose_sayisi+=4
    asal_sayi_orani = ((100/kose_sayisi))*asal_sayisi
    #print(asal_sayi_orani)
    
    sprial_sayisi+=2
print(sprial_sayisi-2) #en son bulunan orandan sonra iki ekleniyor ancak eklenen ikinin oranına bakılmıyor önceki eklenmiş olan 2 bakıldığı için en son olandan 2 eksiltilmeli.








