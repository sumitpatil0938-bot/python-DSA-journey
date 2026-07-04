# append() , insert() , update , remove() , pop() , 

# 1) arr = [10,20,30] 50 ko last mein add karo.
arr = [10,20,30]
arr.append(50)
print(arr)

# 2) arr = [10,20,30] Index 1 par 100 insert karo.
arr = [10,20,30]
arr.insert(1, 100)
print(arr)

# 3) arr = [10,20,30,40] 30 ko 300 se replace karo.
arr = [10,20,30,40]
arr[2]= 300
print(arr)

# 4) arr = [10,20,30,40] 20 ko remove karo.
arr = [10,20,30,40]
arr.remove(20)
print(arr)

# 5) arr = [10,20,30,40,50] Last element delete karo.
arr = [10,20,30,40,50]
arr.pop()
print(arr)

# 6) arr = [10,20,30,40] Output banana hai: [10,100,30]
arr = [10,20,30,40]
arr[1] = 100
arr.pop()
print(arr)