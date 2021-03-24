import math
def circular(x):
    number = []
    for i in range(len(str(x) )):
        y = int((x/(10**(len(str(x))-1)))//1)
        x =((x-(y*(10**(len(str(x))-1))))*10)+y
        number.append(x)
    return number


def prime(x):
    if(x%2 ==0 and x!= 2):
        return 0
    durak = int(math.sqrt(x))+1
    bolen = 3
    while(bolen < durak):
        if(x%bolen == 0):
            return 0
        bolen+=2
    return 1

def bakmaya_gerek_varmi(x):
    x = str(x)
    for i in x:
        if(int(i)%2  == 0 or int(i) == 0):
            return 0
    return 1
def is_circular_prime(dizi):
    for i in dizi:
        if(prime(i) == 0):
            return 0
    return 1

"""
Bir sayının içerisinde iki veya katı varsa eğer o sayının diğer dönüşlerine bakmaya gerek yoktur, çünkü eninde sonunda iki başa gelecektir.

"""

count = 100
kac_tane_var = 13
while(count < 10**6):
    if(bakmaya_gerek_varmi(count) == 1):
        if(is_circular_prime(circular(count)) == 1):
            kac_tane_var+=1
    count+=1
print(kac_tane_var)

    