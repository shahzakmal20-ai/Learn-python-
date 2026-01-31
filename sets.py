print("learn sets in python today")

# sets is a collection of unordered items . but it is immutable or uique, repeated element is stored one

sets1 = {1,2,3,4,5,6,7,"ali",22.4, False,6,7} #duplicate value should be ignored
print(sets1)
print(type(sets1))
print (len(sets1))

print ("how to create empty set")
set2 = set()
print(set2)
print ("important note! \n sets are immutable but its element is cannot be immutable we cannot change the value of its element but also change the intire element")

# method of set 
# 1 add method
set2.add(1)
set2.add(2)
set2.add("name")
set2.add(3)
set2.add(3)
set2.add((5,4,3))
print(set2)
# 2 remove method
set2.remove(3)
print(set2)

# 3 pop method it pop any randam element
set2.pop()
print(set2)
# 4 remove method it can remove all values from set

# set2.remove("name")
# print(set2)

# set2.clear()
# print(set2)

# union method it return all the unique value set from in both sets and 

set3 = {1,3,4,5,6,4,5,(3,6,8)}
set4 = {2,4,6,5,3,(3,6,8,9)}

unionss = set3.union(set4)
print(unionss)

# intersection in set in python it return a matching value in the sets

intersect = set3.intersection(set4)
print(intersect)

values = {
    ("float", 9.0),
    ("integer",9)
}
print(values)