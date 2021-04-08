def basamak_toplam(x):
    x = str(x)
    bst = 0
    for i in x:
        bst += int(i)
    return bst


max_digit_toplam = 0
for i in range(100):
    if(i%10 != 0):
        for j in range(100):
            digit_toplam = basamak_toplam(i**j)
            if(max_digit_toplam < digit_toplam):
                max_digit_toplam = digit_toplam

print(max_digit_toplam)
            