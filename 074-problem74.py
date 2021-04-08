import time
def factorial(x):
    sonuc= 1

    while(x>1):
        sonuc*=x
        x-=1
    return sonuc
def basamak_factorial(x):
    x = str(x)
    fact = 0
    for i in x:
        fact+=factorial(int(i))
    return fact
def daha_once_eklendimi(liste,eklenen):
    for i in liste:
        if(i == eklenen):
            return 1
    return 0
count =146
atmis_uzunluk = 0
start =  time.time()
while(count < 1000000):
    zincir_uzunlugu = []
    zincir_uzunlugu.append(count)
    eklenecek = basamak_factorial(count)
    while(daha_once_eklendimi(zincir_uzunlugu,eklenecek) == 0):
        zincir_uzunlugu.append(eklenecek)
        eklenecek = basamak_factorial(eklenecek)
    if(len(zincir_uzunlugu) == 60):
        atmis_uzunluk +=1
    
    count+=1

end = time.time()
print(atmis_uzunluk)
print(end-start)

    
    
    
    