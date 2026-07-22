# BUBBLE SORT BASICS

# 1) arr = [4,2,3] Pass 1 ke baad array kya hogi?
# --> arr =[4,2,3]
#          [2,4,3] => [2,3,4]

# 2) arr = [3,1,2] Pass 1 ke baad array kya hogi?
# --> arr = [1,3,2]

# 3) arr = [10,5] Kitne comparisons? Kitne swaps?
# --> n - 1 
#     2 - 1 = 1 , therefore there will be 1 comparision and 1 swap

# 4) arr = [1,2,3,4] Already sorted hai. Bubble Sort phir bhi kitne passes lagayega?
# --> n - 1
#     4 - 1 = 3 passes
#     already sorted hai pr fir bhi wo check karega , basic bubble sort main , 
#     agar optimized bubble sort hota to turant rok deta 

# MINI CHALLENGE
# Q) without code answer karo: arr = [7,4,2]
# Pass 1 har comparison likho. Final array after pass 1 ?
# --> arr = [7,4,2] => n - 1 => 3 - 1 = 2
#           [7,4,2] => [4,7,2] => [4,2,7]