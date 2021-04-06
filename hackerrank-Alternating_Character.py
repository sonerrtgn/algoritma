#problem = https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def alternatingCharacters(s):
    kelimeler = []
    uzunluk = len(s)
    count = 0
    silinme = 0
    for i in s:
        kelimeler.append(i)
    while(count < uzunluk-1):
        if(kelimeler[count] == kelimeler[count+1] and kelimeler[count] != "x" ):
            count2 = count+2
            kelimeler[count+1] = "x"
            while(count2 < uzunluk and kelimeler[count] == kelimeler[count2]):
                kelimeler[count2] = "x"
                count2+=1
                silinme+=1
            silinme+=1
        count+=1
    return silinme
