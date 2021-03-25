"""
Sprial :

       [21] 22 23 24[25]
        20 [7] 8 [9] 10
        19  6 [1] 2 11
        18 [5] 4 [3]12
       [17]16 15 14[13]
       5x5 sprial It can be verified that the sum of the numbers on the diagonals is 101.(1+3+5+9+13+17+21+25)
       
       1,9,25,49 -> , n^2, (3)^2 , (5)^2 7^2
       1,7,21,43 =  n^2-(n-1)
       15,17,37 = n^2 -(2*(n-1))
       .
       .
       .

"""
def n_sprial_koseler_toplami(x):
    max_sprial = x*x
    in_sprial = max_sprial-(x-1)
    or_sprial = in_sprial-(x-1)
    min_sprial = or_sprial -(x-1)
    return max_sprial+in_sprial+or_sprial+min_sprial

count = 3
sum_sprial = 1
while(count < 1002):
    sum_sprial += n_sprial_koseler_toplami(count)
    count+=2
print(sum_sprial)
