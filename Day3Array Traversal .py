# 1) arr = [10,20,30,40,50] Traversal karke sab print karo.
arr = [10,20,30,40,50]
num = arr[0]
for num in range(len(arr)):
  print(arr[num])


# 2) arr = [5,10,15,20,25] Sabka sum nikalo.
arr = [5,10,15,20,25]
sum = 0
for num in arr:
    sum += num
print(sum)


# 3) arr = [4,7,2,9,1] Maximum element find karo.
arr = [4,2,9,1]
max_num = arr[0]
for num in (arr):
   if num > max_num:
     max_num = num
print(max_num)


# 4) arr = [4,7,2,9,1] Minimum element find karo.
arr = [4,7,9,1]
min_num = arr[0]
for num in arr:
   if num < min_num:
      min_num = num
print(min_num)

# 5) arr = [10,20,30,40,50] Without using len() Count kitne elements hain.
arr = [10,20,30,40,50]
count = 0 
for num in arr:
   count += 1
print(count)


