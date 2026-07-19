# MIXED SEARCHING QUESTION (LINEAR + BINARY)


# 1) arr = [45, 12, 78, 23, 9] 23 present hai ya nahi ?
arr = [45, 12, 78, 23, 9]
target = 23
found = False
for num in arr:
    if num == target:
       found = True
if found:
   print("found")
else:
   print("Not found")

# 2) arr = [10,20,30,40,50] index value nikalo target = 40 ka 
arr = [10,20,30,40,50]
target = 40
for i in range(len(arr)):
   if arr[i] == target:
      print(i)
      break
   
# 3) arr = [10,20,10,30,10,40] count 3
arr = [10,20,10,30,10,40]
target = 10
count = 0
for num in arr:
   if num == target:
      count =+ 1
print(count)
   
# 4) arr = [5,10,15,10,20] target ka index print karo 
arr = [5,10,15,10,20] 
target = 10
for i in range(len(arr)):
   if arr[i] == target:
      print(i)
      break

# 5) arr = [5,10,15,10,20] target ke last occurance ka index print karo
arr = [5,10,15,10,20]
target = 10
last_index = -1
for i in range(len(arr)):
   if arr[i] == target:
      last_index = i
print(last_index)

# 6) arr = [10,20,30,40,50,60,70] binary search find index
arr = [10,20,30,40,50,60,70]
target = 60
left = 0
right = len(arr)-1
while left < right:
   mid = (left + right)//2

   if arr[mid] == target:
      print(mid)
      break
   elif target > arr[mid]:
      left = mid + 1
   else:
      right = mid - 1

# 7) arr = [10,20,30,40,50] binary serach lago aur target not found print karo
arr = [10,20,30,40,50]
target = 35
left = 0
right = len(arr)-1
found = False
while left < right:
   mid = (left + right)//2
   if arr[mid] == target:
      found = True
      print("found")
      break
   elif target > arr[mid]:
      left = mid + 1
   else:
      right = mid - 1
if not found:
   print("Not Found")

# 8) arr = [10,20,30,40,50] target 50 count binary search steps 
arr = [10,20,30,40,50]
target = 50
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

    
      