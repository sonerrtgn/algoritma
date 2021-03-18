def number_letter(x):
    if(x==100):
        return "hundred"
    
    if(x==20):
        return "twenty"
    if(x==30):
        return "thirty"
    if(x==40):
        return "forty"
    if(x==50):
        return "fifty"
    if(x==60):
        return "sixty"
    if(x==70):
        return "seventy"
    if(x==80):
        return "eighty"
    if(x==90):
        return "ninety"
    
    
    
    if(x==0):
        return  "zero"
    if(x==1):
        return "one"
    if(x==2):
        return "two"
    if(x==3):
        return "three"
    if(x==4):
        return "four"
    if(x==5):
        return "five"
    if(x==6):
        return "six"
    if(x==7):
        return "seven"
    if(x==8):
        return "eight"
    if(x==9):
        return "nine"
    if(x==10):
        return "ten"
    if(x==11):
        return "eleven"
    if(x==12):
        return "twelve"
    if(x==13):
        return "thirteen"
    if(x==14):
        return "fourteen"
    if(x==15):
        return "fifteen"
    if(x==16):
        return "sixteen"
    if(x==17):
        return "seventeen"
    if(x==18):
        return "eighteen"
    if(x==19):
        return "nineteen"
    if(x==1000):
        return "onethousand"

def onluk_yazisi(x):
    if(x<21):
        return number_letter(x)
    x = str(x)
    if(int(x[1])==0):
        return number_letter(int(x[0])*10)
    return number_letter(int(x[0])*10)+number_letter(int(x[1]))

def sayi_yazi_cevir(x):
    if(x<100):
        return onluk_yazisi(x)
    x=str(x)
    if(int(x)%100==0):
        return number_letter(int(x[0]))+number_letter(100)
    y = int(x)-(int(x)//100)*100
    return number_letter(int(x[0]))+number_letter(100)+"and"+onluk_yazisi(y)
count = 1
uzunluk = ""

while(count < 1000):
    #print(sayi_yazi_cevir(count))
    uzunluk += sayi_yazi_cevir(count)
    count+=1

uzunluk+= number_letter(1000)

print(len(uzunluk))
            
        
        
        
        
        
        
        
        
        
        
        