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

c = 9
deneme = 0
bulundumu = 0
while(1):
    a=1
    bulundumu= 0
    while(c> 2*(a*a)):
        primemi = int(c - 2*(a*a))
        if(asalmi(primemi) == 1):
            bulundumu = 1
            break
        a+=1
    if(bulundumu == 0 and asalmi(c) != 1):
        print(c)
        break
    
    c+=2
        

"""
Sayi = asal + 2*(a*a)
asal = sayi + 2*(a*a)
"""