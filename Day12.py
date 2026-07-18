# BINARY SEARCH PROBLEM

# 1) arr = [5,10,15,20,25,30] target 25 ka index value print karo .
arr = [5,10,15,20,25,30]
target = 25
left = 0
right = len(arr)-1

while left <= right:
    mid = (left + right)//2

    if arr[mid] == target:
        print(mid)
        break
    elif target > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1

# 2) arr = [10,20,30,40,50] target 100 print not found .
arr = [10,20,30,40,50]
target = 100
left = 0
right = len(arr)-1
found = False
while left <= right:
    mid = (left + right)//2

    if arr[mid] == target:
        print("found")
        found = True
        break
    elif target > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1
if not found:
    print("not found")

# 3) arr = [10,20,30,40,50,60,70] count steps to find target .
arr = [10,20,30,40,50,60,70]
target = 60
left = 0
right =len(arr)-1
steps = 0
while left <= right:
    mid = (left + right)//2
    steps += 1
    if arr[mid] == target:
        print("find in ",steps,"steps")
        break
    elif target > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1

# 4) user se target lo aur binary search lagao .
arr = [1,2,3,4,5,6,7,8,9,]
num = int(input("Enter Number : "))
target = num
left = 0
right = len(arr)-1
found = False

while left <= right:
    mid = (left + right)//2
    if arr[mid] == target:
        print("found")
        found = True
        break
    elif target > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1
if not found:
    print("Target not found")

# 5) arr = [10,20,30,40,50,60,70] target = 70
# --> Iteration 1:
#     left = 0
#     right = 6
#     mid = (left + right)//2
#     mid = (0 + 6)//2 --> 3
#.    arr[mid] == target
#     40 == 70 --> ❎
#     target > arr[mid]
#     70 > 40 --> ✅
#     left = mid + 1 
#     left = 3 + 1 --> 4
#     right = 6
#     
# --> Iteration 2:
#     left = 4
#     right = 6
#     mid = (left + right)//2
#     mid = (4 + 6)//2 --> 5
#     arr[mid] == target
#     60 == 70 --> ❎
#     target > arr[mid]
#     70 > 60 --> ✅
#     left = mid + 1
#     left = 5 + 1 --> 6
#     right = 6