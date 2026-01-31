print("Today i am learning dictionary datastructure in python 31-01-2026")

dict1 = {
    "name": "Akmal shahzad",
    "age": 22,
    "resut": 92.76,
    "marks" : [80,67,98],
    "passed" : True

}
print(type(dict1))

print("--- Detail of student ---")
print(dict1)
print(dict1["name"])
print(dict1["age"])
print(dict1["resut"])
print(dict1["marks"])
print(dict1["passed"])

print("Sorry Age is Wrong i will correct it ") 
# because dictionary is mutable so that why i change its value of age
dict1["age"] = 20
print(dict1)

# also add come the new key 
dict1["is_adult"] = True
print(dict1)
# also i create a nested dictionary inside my dictionary
dict1["courses"] = {
    "chem" : 40,
    "physics" : 60,
    12 : "math"
}

print(dict1["courses"])

# Dictionar methods that is have 
# 1 print all keys 
print(dict1.keys())
print(len(dict1))
print(list(dict1.keys()))

# 2 Values methods
print(dict1.values())

# 3 items 
print(dict1.items())

# 4 gets method it also return key value but i cannot return error if key not exist

print(dict1.get("courses"))

# 5 update the key value pair in old dictionary

dict1.update({"city": "Hafizabad"})
print (dict1)