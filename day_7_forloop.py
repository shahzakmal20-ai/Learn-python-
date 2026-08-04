# FORLOOPS IN PYTHON

# list1 = ["hello", "world", "python", "loops", "are", "easy"]
# for i in list1:
#     print(i) 
# else:
#     print("The loop on list is  ended")       


# # TUPLE loop IN PYTHON
# tuple1 = (1,2,3,4,5,6,7,8,9)
# for i in tuple1:
#     print(i)
# else:
#     print("The loop on tuple is ended")

# # LOOP ON STRING IN PYTHON

# string1 = "Hello World"
# for i in string1:
#     print(i)
# else:
#     print("The loop on string is ended")



# name = "helloworld"
# for i in name:
#     if i == "l":
#         print("The letter is found in the string")
#         break
# else:
#     print("The letter is not found in the string")


# PRACTICE QUESTIONS

# nums = [1,4,9,16,25,36,49,64,81,100]
# for i in nums:
#     print(i)

# nums = (1,4,9,16,25,1000,36,49,64,81,1000,1000)
# x = 1000
# idx = 0
# for i in nums:
#     if i == x:
#        print("The number is found in the tuple at index: ",idx)
#     idx+=1


# =====================================================RANGE FUNCTION IN PYTHON=====================================================
# range(start, stop, step)

# print("The range function in python is used to generate a sequence of numbers. It can take up to three arguments: start, stop, and step. The start argument specifies the starting number of the sequence (inclusive), the stop argument specifies the ending number of the sequence (exclusive), and the step argument specifies the difference between each number in the sequence. If only one argument is provided, it is treated as the stop value, and the start value defaults to 0. If two arguments are provided, they are treated as the start and stop values, and the step value defaults to 1. If all three arguments are provided, they are used as specified.")
# print(range(10))

# seq = range(10)
# for i in seq:
#     print(i)

# for i in range(10):#range(stop)
#     print(i)

# for i in range(5, 10): #range(start, stop)
#     print("its start from: ",i)

# for i in range(0, 10, 2): #range(start, stop, step)
#     print("its start from: ",i)



# for i in range(0, 10, 2): #range(start, stop, step)
#     print("all even numbers ",i)


# for i in range(1,101): #range(start, stop, step)
#     print(i)

# for i in range(100,0,-1): #range(start, stop, step)
#     print(i)

# n = 5
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")


# ==============================================PASS STATEMENT IN PYTHON========================================================

# for i in range(10):
#     if i%2 == 0:
#         pass
#     else:
#         print(i)

# for i in range(10):
#     pass
# print("The loop is ended")




# =========================================PRACTICE QUESTIONS ON FORLOOPS OR WHILE LOOP IN PYTHON========================================================
# sum of n numbers using while loop
# idx = 0
# n = 5
# sum = 0
# while idx <=n:
#     sum += idx
#     idx += 1
# print(sum)

# n = 6
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(f"The factorial of {n} is: {fact}")
    
# FIND THE PRIME NUMBER FROM 1 TO N USING FORLOOP
n = 20
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{i} is a prime number")