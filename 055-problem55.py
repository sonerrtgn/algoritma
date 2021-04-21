def palindrom(x):
    x = str(x)
    uzunluk = len(str(x))
    count = 0
    while(count < uzunluk):
        #print(count,count)
        if(x[count] != x[uzunluk-count -1]):
            return -1
        count+=1
    return 1

def lyrcelmi(x):
    tersi =int(str(x)[::-1])
    sayi = 1
    while(sayi<49):
        x = x+tersi
        tersi =int(str(x)[::-1])
        #print(x)
        #print(sayi,"yenileme",x)
        if(palindrom(x) ==1 ):
            return -1
        sayi+=1
    return 1

sayi = 0
count =0
while(count < 10**4+1):
    if(lyrcelmi(count)==1):
        sayi+=1
        #print(count,end="")

    count+=1
print(sayi)


#print(lyrcelmi(349))
