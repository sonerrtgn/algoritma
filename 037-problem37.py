import math
def prime(x):
    if(x%2 ==0 and x!= 2):
        return 0
    if(x==1):
        return 0
    durak = int(math.sqrt(x))+1
    bolen = 3
    while(bolen < durak):
        if(x%bolen == 0):
            return 0
        bolen+=2
    return 1


def kesilince_urunler(x):
    x= str(x)
    uzunluk = len(x)
    urunler = []
    for i in range(uzunluk):
        urun = ""
        while(i < uzunluk):
            urun+= x[i]
            i+=1
        urunler.append(int(urun))
    uzunluk-=1
    while(uzunluk>0):
        count = 0
        urun = ""
        while(count <uzunluk):
            urun+=x[count]
            count+=1
        urunler.append(int(urun))
        uzunluk-=1
        
    return urunler

def urunler_asalmi(x):
    uzunluk = len(x)-1
    while(uzunluk>-1):
        if(prime(x[uzunluk]) == 0):
            return 0
        uzunluk-=1
    return 1

bulunan_asallar = 0
count = 10
asallar_toplami = 0
while(bulunan_asallar <11):
    if(urunler_asalmi(kesilince_urunler(count)) ==1):
        bulunan_asallar+=1
        asallar_toplami += count
        print(count)
    count+=1
    
print(asallar_toplami)

