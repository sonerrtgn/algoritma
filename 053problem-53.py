def factorial(x):
    sonuc = 1
    while(1<x):
        sonuc*=x
        x-=1
    return sonuc
    
def kombin(x,y):
    return factorial(x)/ (factorial(y)*factorial(x-y))
    
n = 1
r = 1
deger_sayisi = 0
while(n<101):
    r=0
    while(r<=n):
        if(1000000 < kombin(n,r)):
            deger_sayisi+=1
            print(n,r)
        r+=1
    n+=1
print("Toplam deger sayisi : ",deger_sayisi)