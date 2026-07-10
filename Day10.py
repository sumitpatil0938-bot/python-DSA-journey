#  BINARY SEARCH INTRODUCTION

# 1) arr = [10,20,30,40,50] find middle index ?
arr = [10,20,30,40,50]
left = 0
right = len(arr)-1
mid = (left + right)//2
print(mid)


# 2) arr = [10,20,30,40,50] find middle element ?
arr = [10,20,30,40,50]
mid =(left + right)//2
print(arr[mid])


# 3) arr = [5,10,15,20,25,30,35] target 25 ?
arr = [5,10,15,20,25,30,35]
target = 25
left = 0
right = len(arr)-1

while left <= right:
    mid = (left + right)//2

    if arr[mid] == target:
        print(arr[mid])
        break
    elif target > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1

# mid = ( left + right)//2
# compare arr[mid] == target
# left = mid + 1
# right = mid - 1 


# 4) Why Binary Search needs sorted array ?
# --> Binaray search need sorted array because, on each and every step it breaks array into two parts to find target , 
# if there is no sorted array , unsorted array then binary search will not work because numbers are arrange in unsorted form
# to break it from middle into every step it need sorted array
# sorted array --> arr = [10,20,30,40,50,60,70,80,90,100]
# unsorted array --> arr = [20,60,50,70,10,80,30,90,40,100]
# so we can break sorted array from mid until we get's target


# 5) Linear Search vs Binary Search ?
# --> A) Linear search = linear serach travers array means, it check each and evary element present in array
#                        it check it dosent care whether it is sorted or unsorted array because it satrt's from starting and 
#                        goes upto end , with continue checking of every element , when it get's it true condition or target , it break 
#      
#     B) Binary search = in binary search as i know it need's sorted array because at each and every step until it gets's condition true it work's 
#                        means working on breakig array into 2 parts 
#                         
