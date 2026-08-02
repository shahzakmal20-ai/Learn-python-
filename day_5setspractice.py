# ecomerce product tagging System
# ===============================================
# PRACTICE PROBLEM OF DAY 5 FOR SETS LECTURE
# ===============================================

summer_collection = {"cotton", "casual", "breathable", "t-shirt", "cotton"}
sports_wear = {"breathable", "shorts", "t-shirt", "polyester", "flexible"}
print(summer_collection , sports_wear)

print("Common products in both: ", summer_collection.intersection(sports_wear))

print("Unique products from both sets: ", summer_collection.union(sports_wear))

print("The difference between both sets: ", summer_collection - sports_wear)
print("The difference between both sets: ", summer_collection.difference(sports_wear))

summer_collection.add("linen")

print("afte addition new product: ", summer_collection)

summer_collection.remove("casual")

print("After removing the product: ", summer_collection)

