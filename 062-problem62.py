"""
problem link -> https://projecteuler.net/problem=62
->Soruda ilk yakaladigim nokta kombinasyonları olabilmek icin aynı basamak sayisina sahip olmalaridir
->bir sayıdan baslayip o sayiyi bir bir arttirip bu sayiya kombinasyonları mı diye bakarak bu problemi cozmeye calisiyorum.
->herhangi bir sayıdan baslayip nereye kadar gidecegimizi bilmiyoruz ancak bir sayidan basladiktan sonra sayet basamak sayisi
bir artarsa ondan daha buyuk sayılara bakmaya gerek yoktur, cünkü basamak sayısı olarak buyuk bir sayı hicbir zaman kombinasyonu olamaz.
---ornek---
15 sayisi ornek icin baslangic degeri olsun.
15^3 = 3375
simdi bir bir arttiralim.
16^3 = 4096 halen bakmaya devam edebiliriz cunku yeni sayimiz halen 4 basamaklı bu demek oluyorki kombinasyn olma ihtimali halen var.
17^3 = 4913 halen bakmaya devam edebilriz.
18^3 = 5832 halen bakilabilir.
19^3 = 6859 devam..
20^3 = 8000 
21^3 = 9261
22^3 = 10648 artik bakmaya devam etmeye gerek yok cunku bundan sonraki butun sayilar artik kombinasyon olusturamaz.

durak noktasını kavradiktan sonra uygulamak kolaylasiyor.

tahmini calisma suresi 70-80 saniye 60 saniyenin altinda degil ama bence yinede kabul edilebilir bir cozum :)

"""

import time


def permutasyonmu(sayi_1,sayi_2):
    sayi_1_str = str(sayi_1)
    sayi_2_str = str(sayi_2)
    if(len(sayi_2_str) != len(sayi_1_str)):
        return -1 #Burdan sonra devam etmeye gerek olmadığını anlamak için -1 return ediliyor.
    sayi_1_sayilar = [0]*10 #Burada sayi_1'de bulunan sayıların kaç tane oldugunu hesaplamak için bir dizi olusturuluyor.
    sayi_2_sayilar = [0]*10
    for i in range(len(sayi_1_str)):
        """
        girilen sayıların basamaklarına tek tek bakılıyor, basamak şayet 3 ise 3.elemana 1 ekleniyor buda bize 3'ten
        kaç tane oldugunu bildiriyor.
        """
        sayi_1_sayilar[ int(sayi_1_str[i]) ]+=1
        sayi_2_sayilar[ int(sayi_2_str[i]) ]+=1
    for i in range(10):
        if(sayi_1_sayilar[i] != sayi_2_sayilar[i]):
            return 0 #burada basamak sayıları aynı ancak kombinasyon olmadığını anlıyoruz.
    
    return 1 # buda uyugn olayn sayıyı buldugumuz manasına gelir.

start = time.time()
baslangic = 1
kup_sayisi = 0
while(kup_sayisi != 5):
    sayi_1 = baslangic**3 # python -> a**2 = a^2
    sayi_2 = baslangic+1
    permutasyon_sonuc = permutasyonmu(sayi_1,sayi_2**3)
    bakilan_kup_sayisi = 1 #bakilan sayinin kendisinide aldigimiz icin 1'den baslatiyorum.
    #her sayıdan sonra basamak sayısı artmamak koşuluyula onları bir donguye koyup kac tane kombinasyonu oldugunu buluyorum.
    while(permutasyon_sonuc != -1):
        #ikinci bakılan sayı basamak sayısından daha büyük olmadıkça bu döngü gerçekleşmeli.
        if(permutasyon_sonuc == 1):
            bakilan_kup_sayisi +=1
        sayi_2+=1
        permutasyon_sonuc = permutasyonmu(sayi_1,sayi_2**3) #permutasyonu burda bir kez hesaplatıyorum, direk fonksiyonu çağırırsam iki kez kullanmış olacağum bunu yapmak bana bir işlemi iki kez kontrol etmek yerine bir kez kontrol etme avantajı sağlıyor.
    if(kup_sayisi < bakilan_kup_sayisi):
        kup_sayisi = bakilan_kup_sayisi 
    baslangic+=1
    
    #if(bakilan_kup_sayisi > 2):
    #    print(sayi_1,bakilan_kup_sayisi)

end = time.time()
print("gecen sure: ",end-start)    
            
        