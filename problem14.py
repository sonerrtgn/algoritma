colatz_dizi = []
colatz_dizi.append(0)
colatz_dizi.append(1)
colatz_dizi.append(2)


count = 3
max_uzunluk = 0
max_uzunlugu_veren_zincir=0
while(count < 1000000):
    koruma = count
    colat_uzunluk = 1
    while(koruma !=1):
        if(koruma%2==0):
            koruma=koruma/2
            if(koruma<count):
                colat_uzunluk= colat_uzunluk+colatz_dizi[int(koruma)]
                colatz_dizi.append(colat_uzunluk)
                if(max_uzunluk<colat_uzunluk):
                    max_uzunluk  =colat_uzunluk
                    max_uzunlugu_veren_zincir = count
                break
        else:
            koruma = koruma*3+1
        colat_uzunluk=colat_uzunluk+1        
    count=count+1
                
      
print("Max uzunluk:",max_uzunluk,"Max uzunlugu veren zincir: ",max_uzunlugu_veren_zincir)


    
