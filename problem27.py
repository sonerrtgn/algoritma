import math

def quadrtik(n,a,b):
    return (n*n+a*n+b)
def prime(x):
    if(x%2 == 0 and x!=2):
        return 0
    if(x<1):
        return 0
    bolen=3
    kok = math.sqrt(x)+1
    while(bolen < kok):
        if(x%bolen == 0):
            return 0
        bolen+=2
    return 1

def bu_fonksiyon_kac_asal_uretir(a,b):
    count =1
    while(prime(quadrtik(count,a,b)) == 1):
        count+=1
    return count-1



a = -1001
b = -1001
a_max =0
b_max= 0
max_prime_sayisi = 0
while(a<1001):
    b=0
    while(b<1001):
        if(bu_fonksiyon_kac_asal_uretir(a,b) > max_prime_sayisi):
            max_prime_sayisi = bu_fonksiyon_kac_asal_uretir(a,b)
            max_a= a
            max_b= b
        b+=1
    a+=1
    
print(max_a*max_b)
    
    
    
        
    










