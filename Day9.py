# ADVANCE LINEAR SEARCH

# 1) arr = [5,10,5,15,5] target = 5 find all position ?
arr = [5,10,5,15,5]
target = 5
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
    
# 2) arr = [2,4,7,9,10,12] count even number ?
arr = [2,4,7,9,10,12]
count = 0
for num in arr:
    if num % 2 == 0:
        count += 1
print(count)

# 3) arr = [2,4,7,9,10,12] count odd numbers ?
arr = [2,4,7,9,10,12]
count = 0
for num in arr:
    if num % 2 != 0:
        count += 1
print(count)

# 4) arr = [100,250,50,400,75] find maximum ?
arr = [100,250,50,400,75]
max_num = arr[0]
for num in arr:
    if num > max_num:
        max_num = num
print(max_num)

# 5) arr = [100,250,50,400,75] find minimum ?
arr = [100,250,50,400,75]
min_num = arr[0]
for num in arr:
    if num < min_num:
        min_num = num
print(min_num)

# 6) arr = [100,250,50,400,75] searching using user input ?
arr = [ ]
for i in range(1):
    num = int(input("Enter number : "))
    arr.append(num)

target = int(input("Enter target : "))

found = False

for num in arr:
     
     if num == target:
        found = True
        break
        
if found:
    print("Yes")
else:
    print("Not")

# 7) Array mein 5 numbers lo, target lo, aur sirf “Found” nahi balki target kis index par mila wo bhi print karo ?
arr = []

for i in range(5):
    num = int(input("Enter number : "))
    arr.append(num)

print(arr)

target = int(input("Enter target : "))

found = False

for i in range(len(arr)):

    if arr[i] == target:
        found = True
        print("Index Number :", i)
        break

if found:
    print("Yes")
else:
    print("No")