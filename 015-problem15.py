"""
2x2 'lik bir ızgarada bir uctan bir uca gitmek için 2 birim sağ ve 2 birim alt yapılmak zorunludur:
Sağ ve Alt'ın kısaltmaları S ve A
SS AA
toplam olay 4! ancak iki durum aynı olduğu için(1ve2 yer değiştirse dahi yine ss aa olduğu gibi) olduğu için
4!/(2!*2!) şeklinde bulunur.

20*20 lik bir ızgarada 20 birim sağ yirmi birim alt yapılması zorunludur buda:
40!/(20!*20!) eşittir.

"""
#Sadeleştirme yaparak ilk 20! faktöriyeli sadeleştirip geri kalanlarına birbirine bölerek çarpa çarpa gidiyoruz.
ust_deger = 40
alt_deger = 20
sonuc= 1
while(ust_deger>20):
    sonuc = sonuc*(ust_deger/alt_deger)
    ust_deger = ust_deger-1
    alt_deger = alt_deger-1
print(sonuc)

#direk bulmak
def fakt(x):
    sonuc = 1
    while(x!=1):
        sonuc=sonuc*x
        x=x-1
    return sonuc
        
print(fakt(40)/(fakt(20)*fakt(20)))
    
    
    
    
