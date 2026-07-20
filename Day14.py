# REVISION + QUIZE + INTERVIEW ROUND

# ROUND 1 ( RAPID FIRE QUESTION)

# 1) Array kya hota hai ?
# --> list hoti hai jise ham array ke form main save karte hai

# 2) Negative indexing mein: arr[-1] kya return karega?
# --> array  ka last number

# 3) Traversal kya hota hai?
# --> Array ke eliments ko ek ek karke chek karna .

# 4) Append ka use kab karte hain?
# --> jab array ke end main kuch add karna ho .

# 5) Max element find karne ka basic logic kya hai?
# --> max_num = arr[0]

# 6) Linear Search ka use kab karte hain?
# --> jab hamare pass unsorted array ho ya fir kam data ho tab .

# 7) Linear Search ki Worst Case Time Complexity?
# --> o(n)

# 8) Binary Search ki sabse important condition?
# --> array must be sorted .

# 9) Binary Search ka Mid Formula?
# --> mid = (left + right)//2

# 10) target bada ho target > arr[mid] to kya karte hai?
# --> left = mid + 1


# ROUND 2 (DRY RUN CHALLENGE)

# 1) arr = [10,20,30,40,50] target = 40 Linear Search mein kitne comparisons lagenge?
# --> 3 search

# 2) arr = [10,20,30,40,50] target = 30 Binary Search mein kitne steps lagenge?
# --> found in 1 step 

# 3) arr = [10,20,30,40,50] target = 15 Binary Search mein final:
# left = ? , right = ? jab search finish hogi?
# --> left = 1 , right = 0


# ROUND 3 ( LOGIC QUESTION)

# 1) arr = [5,10,5,20,5] target = 5 Count Occurrence?
# --> count =+ 1 logic hai 

# 2) arr = [10,20,30,20,40] target = 20 First Occurrence? , Last Occurrence?
# --> first occurance = if arr[mid] == target 
# --> last occurance = last_index = -1
#                      last_index = i

# 3) arr = [50,10,30,20] target = 20 Linear Search ya Binary Search? Aur kyu?
# --> linear search , kyu ki array unsorted hai.


# ROUND 4 (LEVEL 3 INTERVIEW)

# 1) Linear Search aur Binary Search mein difference explain karo.
# --> linear serach works on unsorted and sorted array both 
# --> binary search work only on sorted array 

# 2) Agar array sorted nahi hai to Binary Search kyu fail ho sakti hai?
# --> kabhi nahi 

# 3) Agar array mein 1,000,000 elements hain: Kaunsa search choose karoge? Aur kyu?
# --> binary serach , kyu ki output jaldi se dhumd nikalta hai time complexitya O (log n)

# 4) Best Case Complexity: Binary Search = ? , Linear Search = ?
# --> Binary serach = O(log n)
# --> Linear search = O(1)


# FINAL BOSS QUESTION 
# without code .

# Q) arr = [10,20,30,40,50,60,70] target = 60 Found in ? steps ?

#Iteration 1:
#left = 0
#right = 6
#mid = 3
#arr[mid] = 40

#Iteration 2:
#left = 4
#right = 6
#mid = 5
#arr[mid] = 60

# --> steps(iteration) = 2
# aage jane ke jarurat nahi hai 

#Iteration 3:
#left =
#right =
#mid =
#arr[mid] =