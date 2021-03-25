def pandigital(x):
    count = 1
    i=0
    uzunluk = len(x)
    if(len(x)<9):
        return -1
    if(len(x)>9):
        return -2
    while(i<uzunluk):
        if(count == int(x[i])):
            count+=1
            i = -1
        i+=1
    if(count==10):
        return 1
    return 0

"""
10000*1 -> 10000
100000*2 -> 20000
'20000'+'10000'  = 10basamaklı oldugu için bu sayılardan daha büyüklerine bakmaya gerek yoktur

"""

count = 1
max_pand = 0
while(count < 10000):
    carpan = 1
    sayi = ""
    while(pandigital(sayi) == -1):
        sayi += str(count*carpan)
        carpan+=1
    if(pandigital(sayi) == 1):
        if(max_pand < int(sayi)):
            max_pand = int(sayi)
    count+=1
    
print(max_pand)
        

            
            