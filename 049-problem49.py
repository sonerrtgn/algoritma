import math

def permute(sayi1,sayi2):
    sayi1 = str(sayi1)
    sayi2 = str(sayi2)
    for i in sayi1:
        for j in sayi2:
            if(j == i):
                break
        else:
            return False
    for i in sayi2:
        for j in sayi1:
            if(j == i):
                break
        else:
            return False
    return True
def asalmi(sayi):
    if(sayi%2  == 0):
        return False
    bolen =3
    kok = math.sqrt(sayi)//1 +1
    while(bolen < kok):
        if(sayi%bolen == 0):
            return False
        bolen +=2
    return True

baslangic = 1000
durak = 10000
while(baslangic < durak):
    baslangic2 = baslangic
    artis_mik  = 1
    while(baslangic2+2*artis_mik< durak):
        if(permute(baslangic,baslangic+artis_mik)):
            if(permute(baslangic,baslangic+2*artis_mik)):
               if(asalmi(baslangic)):
                   if(asalmi(baslangic+artis_mik)):
                       if(asalmi(baslangic+2*artis_mik)):
                           print(baslangic, " ",(baslangic+artis_mik)," ",(baslangic+2*artis_mik))
                           
        artis_mik+=1
    baslangic+=1
    
                