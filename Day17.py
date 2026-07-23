# BUBBLE SORT PROBLEM

# 1) dry run karo: arr = [8,5,2] pass 1ke baad array ??
# -> arr = [8,5,2] pass 1
#    [5,8,2] swap 1
#    [5,2,8] swap 2

# 2) Dry Run karo: arr = [4,1,3] Final sorted array?
# -> arr = [4,1,3] (n-1) = (3-1) = 2 pass
#    pass 1 => arr = [4,1,3]
#                    [1,4,3] swap 1
#                    [1,3,4] swap 2

# 3) Answer do: 5 elements bubble sort kitne passes ?
# -> 5 element = n
#    n - 1 = 5 - 1 = 4 
# total 4 pass

# 4) Answer do: Bubble Sort 7 elements Maximum comparisons in one pass?
# -> 1 pass main 
#    6 comparision hoge 

# 5) Fill in the blank: if arr[j] > ________:
# -> if arr[j] > arr[j+1]


# NOTES
# -> Adjacent element compare karta hai.
# -> Left > Right ho to swao.
# -> Har pass ke baad largest elemant end mein chala jata hai.
# -> Total pass = n - 1
# -> Basic bubble sort time complexity =  O(n²)
# -> Space complexity = O(1)
# -> stable sorting algorithm


# MINI CHALLENGE 
# without running code solve manually solve : arr = [9, 4, 7, 2]
# pass 1 ke baad array ? => arr = [4,7,2,9]
# pass 2 ke baad array ? => arr = [4,2,7,9]
# final sorted array ? => arr = [2,4,7,9]
# total pass ? => n - 1 => 4 - 1 = 3 passes
# n = ? => n = 4