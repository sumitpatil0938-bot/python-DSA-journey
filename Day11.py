# BINARY SEARCH CODING

# 1) arr = [5,10,15,20,25,30,35] binary search lagao aur target 30 found karo ?
arr = [5,10,15,20,25,30,35]
target = 30
left = 0 
right = len(arr)-1

while left <= right:
    mid = (left + right)//2

    if arr[mid] == target:
       print("found")
       break

    elif target > arr[mid]:
      left = mid + 1
    else:
       rignt = mid - 1


# 2) arr = [10,20,30,40,50] binary search lago target not found ?
arr = [10,20,30,40,50]
target = 15
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
   print("Not found")


# 3) arr = [10,20,30,40,50] target = 40 , target mila to index print kar do ?
arr = [10,20,30,40,50]
target = 40
left = 0
right = len(arr)-1

while left <= target:
   mid = (left + right)//2

   if arr[mid] == target:
      print(mid)
      break
   
   elif target > arr[mid]:
      left = mid + 1
    
   else:
      right = mid - 1


# 4) creat array , take target from user and binary search lagao ?
array = []
for i in range(3):
   num1 = int(input("Enter number1 : "))
   array.append(num1)
   print(array)

num2 = int(input("Enter number2 : "))
target = num2
left = 0
right = len(array)-1

found = False

while left <= right:
   mid = (left + right)//2

   if array[mid] == target:
      print("found")
      found = True
      break
   elif target > array[mid]:
      left = mid + 1
   else:
      right = mid - 1

if not found:
   print("not found")


# 5) creat array , count karo binary search ko kitne steps lage ?
array = []
for i in range(7):
   num1 = int(input("Enter number1 : "))
   array.append(num1)
   print(array)
num2 = int(input("Enter number2 : "))
target = num2

left = 0
right = len(array)-1
steps = 0

while left <= right:
    steps += 1
    mid = (left + right)//2

    if array[mid] == target:
        print("Found in", steps, "steps")
        break

    elif target > array[mid]:
        left = mid + 1

    else:
        right = mid - 1





