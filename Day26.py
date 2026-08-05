# REVERSE STRING & CHARACTER FREQUENCY

# 1) word = "dog" reverse ?
# -->  god

# 2) word = "apple" reverse ?
# --> elppa

# 3) word = "mom" frequency ?
# --> m = 2
#     0 = 1

# 4) word = "banana" frequency ?
# --> b = 1
#     a = 3
#     n = 2

# 5) word = "level" reverse ?
# --> level



# MINI CHALLENGE 

# 1) word = "cyber" reverse ?
# --> rebyc

# 2) word = "hello" frequency ?
# --> h = 1
#     e = 1
#     l = 2
#     o = 1

# 3) word = "aaaab" freruency ?
# --> a = 4
#     b = 1

# 4) word = "12321" reverse ?
# --> 12321

# 5) word = "program" first character frequency ?
# --> p = 1



# REVISION NOTES

# method 1
# --> word[::-1]

# method 2
# --> reverse = ""
#     for ch in word:
#         reverse = ch + reverse 

# method 3
# --> freq{}
#     for ch in word:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#              freq[ch] = 1

# time complexity
# revrese O(n)
# frequency O(n)