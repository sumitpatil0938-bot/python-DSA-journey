# REVISION DAY 
# Day 1 - Day 6
# Question solving 

# 1) arr = [5,10,15,20,25] print all elements 
arr = [5,10,15,20,25]
for num in arr:
    print(num)

# 2) arr = [5,10,15,20,25] sum find karo 
arr = [5,10,15,20,25]
sum = 0
for num in arr:
     sum += num
print(sum)

# 3) arr = [5,10,15,20,25] count fond karo 
arr = [5,10,15,20,25]
count = 0
for num in arr:
    count += 1
print(count)

# 4) arr = [5,10,15,20,25] maximum find karo
arr = [5,10,15,20,25]
max_num = arr[0]
for num in arr:
    if num > max_num:
        max_num = num
print(max_num)

# 5) arr = [5,10,15,20,25] min find karo 
arr = [5,10,15,20,25]
min_num = arr[0]
for num in arr:
    if num < min_num:
     min_num = num
print(min_num)

# 6) arr = [5,10,15,20,25] linear search lagao target = 20 
arr = [5,10,15,20,25]
target = 20
for i in range(len(arr)):
     if arr[i] == target:
      print(i)
      break
