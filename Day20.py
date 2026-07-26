# MERGE SORT ( Divide & Conquer)

# 1) Array ko sirf divide karo arr = [6,2,8,1]
# --> arr = [6,2,8,1]
#     arr = [6,2] [8,1]
#     arr = [6],[2],[8],[1]

# 2) [5] , [1] Merge karne ke baad output?
# --> arr = [1,5]

# 3) Left = [2,7] , Right = [3,8] Merge manually ?
# --> [2,7] [3,8]
#     2 vs 3 = 2 
#     3 vs 7 = 3
#     7 vs 8 = 7
#     remaining one is 8 add at last 

# 4) final soerted array ? arr = [9,4,6,2]
# --> arr = [9,4,6,2]
#     arr = [2,4,6,9] final sorted array .


# NOTES 
# - Merge sort = divide & conquer.
# - Merge main hamesha dono arrays ke samallest elements compare katro. 
# - Best = O(n log n).
# - Worst = O(n log n).
# - Space = O(n)
# - Stable sorting algorithm hai.

# Q) Dary run [7,2,6,4]
# arr = [7,2,6,4]
# ↓
# [7,2]  [6,4]
# ↓
# [7] [2]  [6] [4]
# ↓
# [2,7]  [4,6]
# ↓
# 2 vs 4 → 2
# 7 vs 4 → 4
# 7 vs 6 → 6
# remaining → 7
# ↓
# [2,4,6,7]