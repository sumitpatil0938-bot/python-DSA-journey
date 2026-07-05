# MAX AND MIN ELEMENT

# 1) arr = [12, 45, 7, 89, 23] Maximum element find karo.
array = [12, 45, 7, 89, 23] 
max_num = array[0]
for num in (array):
    if num > max_num:
     max_num = num
print("Number = " , max_num)

# 2) arr = [12, 45, 7, 89, 23] Minimum element find karo.
array = [12, 45, 7, 89, 23] 
min_num = array[0]
for num in (array):
    if num < min_num:
     min_num = num
print("Number = " , min_num)

# 3) arr = [100, 20, 300, 40, 500] Maximum aur minimum dono find karo.
array = [12, 45, 7, 89, 23] 
min_num = array[0]
max_num = array[0]
for num in (array):
    if num < min_num:
     min_num = num
    if num > max_num:
     max_num = num
print("Maximum = " , min_num)
print("Minimum = " , max_num)

# 4) arr = [-10, -5, -20, -1] Maximum find karo.
array = [-10, -5, -20, -1]
max_num = array[0]
for num in (array):
  if num > max_num:
    max_num = num
print(max_num)

# 5) arr = [8] Max and Min print karo.
array = [8]
min_num = array[0]
max_num = array[0]
for num in (array):
    if num < min_num:
     min_num = num
    if num > max_num:
     max_num = num
print("Maximum = " , min_num)
print("Minimum = " , max_num)