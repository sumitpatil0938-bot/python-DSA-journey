# LINEAR SEARCH THEORY

# 1) arr = [5,10,15,20,25] target 15 ?
arr = [5,10,15,20,25]
target = 15
found = False
for num in arr:
    if num == target:
        found = True
if found:
    print("Found")
else:
    print("Not found")


# 2) arr = [5,10,15,20,25] find index of "20" ?
arr = [5,10,15,20,25]
target = 20
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break


# 3) arr = [10,20,20,30,20,40] count occurance target 20 ?
arr = [10,20,20,30,20,40]
count = 0
for num in arr:
    if num == target:
        count += 1
print(count)


# 4) arr = [7,14,21,14,28] find first occurance target 14 ?
arr = [7,14,21,14,28]
target = 14
for i in range(len(arr)):
    if arr[i] == target:
      print(i)
      break


# 5) arr = [7,14,21,14,28] find last occurance target 14 ?
arr = [7,14,21,14,28]
last_index = -1
for i in range(len(arr)):
    if arr[i] == target:
        last_index = i
        print(last_index)
        break
        
