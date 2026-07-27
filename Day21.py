# MERGE SORT CODE + RECURSION

# 1) arr=[9,3,8,2] sirf divide karo ?
# --> arr=[9,3,8,2]
# [9,3] [8,2]
# [9] [3] [8] [2]

# 2) merge manually left = [2,7],right = [1,5] 
# --> 2 vs 1 = 1
#     2 vs 5 = 2  
#     7 vs 5 = 5
#     remaining one is 7 at last 

# 3) merge function main i kis array ko point karta hai ?
# --> i = left array

# 4) merge function main j kis array ko point karta hai ?
# --> j = right array

# 5) merge function main k kis array ko point karta hai ?
# --> k = original array 

# COMPLETE CODE OF MERGE SORT 

def merge_sort(arr):
    if len(arr) <= 1:   
        return        # yaha tak array sorted ho chuka hai , aage divide karne ke jarurat nahi hai
                      # return yaha pe recursion ko rok deta hai.
    
    mid = len(arr) // 2    # array ki length count karta hai aur maid main se break karta hai

    left = arr[:mid]    # yaha pe sort hota hai left side array
    right = arr[mid:]    # yaha pe sort hota hai right side array

    merge_sort(left)    # yaha pe recursive call left ko 
    merge_sort(right)     # yaha pe recursive call left ko 

    i = 0    # left array ka pointer
    j = 0    # right array ka pointer
    k = 0    # original array ka pointer

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]

        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
# RIVISION NOTES 
# - merge sort = Divide & conquer
# - recursion = Function calling itself
# - base case = len(arr)<=1
# - mid = len(arr)//2
# - left = arr[:mid]
# - right = arr[mid:]
# - merge_sort(left)
# - merge_sort(right)
# - i = left array ko pointer karta hai 
# - j = right array ko pointer karta hai 
# - k = original array ko pointer karta hai 
# - Time complexity = O(n log n)
# - pace complexity = O(n)
# - Stable sorting algorithm hai 
# - Not in palce 