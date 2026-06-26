#  ARRAY 

# Q1) arr = [5, 10, 15, 20, 25] print first element and last element
num = [5,10,15,20,25]
print (num[0]) # 5
print (num[-1]) # 25



# Q2) arr = [1, 2, 3, 4, 5] replace 3 with 100
num = [1, 2, 3, 4, 5]
num[2] = 100
print(num)  # [1, 2, 100, 5]



# Q3) take numbers from users and put it into list 
array =[]
for i in range(5):
  num = int(input("Enter numbers : "))
  array.append(num)
print(array) # [1, 2, 3, 4, 5]



# Q4) list ka size print kro arr = [1, 2, 3, 4, 5]
arr = [1, 2, 3, 4, 5]
print(len(arr)) # 5 



# Q5) Array ke saare elements print karo using loop.
array = [2, 4, 6, 8, 10]
for num in array:
 print(num)



# ab isme hamne use sekha hai  and problem bhi solve kiya 
# jo concept mujhe samaj nahi aaraha tha 


# [ for i in range()] kya hota and use case 
#  ye jo hai i in range ka concept ye batata hai pytho ko kaha se shurun kare aur kaha pe khata ek range batata hai 
# to isme jo i hai to index vale bata ta hai 

      
# .append 
# ye jo .append hai wo list main without any change last main values add karyta hai .append()


# Kisi existing element ko change karna ho → arr[index] = value


# TOPIC COVER TODAY

# Array (Python List) kya hoti hai
#Indexing
# Negative Indexing
# Update Elements
# len()
# Traversal
# for loop basics
# range()
#append()