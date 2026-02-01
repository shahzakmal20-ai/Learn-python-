# loop are used that actions i want to repeated
count = 1
while count < 6:
    print("count is: ",count)
    count+=1

# program to print the table of entered number
table = 5
count = 1
while count <= 10:
    print(count,"X",table,"= ",count*table)
    count+=1


# programm print the value of the list
lis = [1,3,5,6,7,87,3,65]
l = len(lis)
x = 3
count = 0
while count < l:
    if lis[count] == x:
      print("items is : ",lis[count])
      print("found at index: ",count)
    else:
       print("finding..")
    count += 1