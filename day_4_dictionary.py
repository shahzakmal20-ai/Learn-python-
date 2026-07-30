info = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Engineer",
    "is_active": True,
    "email": "john.doe@example.com",
    "skills": ("Python", "JavaScript", "SQL"),
    "hobbies": ["Reading", "Hiking", "Gaming"]
}

print("User Information:", info)
print(type(info))
print("Name:", info["name"])
print("Age:", info["age"])
print("Occupation:", info["occupation"])
print("Is Active:", info["is_active"])
print("Email:", info["email"])
print("Skills:", info["skills"])
print("Hobbies:", info["hobbies"])  


info["name"] = "Jane Smith"
print("Updated Name:", info["name"])
info["hobbies"][1] = "Traveling"
print("Updated Hobbies:", info["hobbies"])
print(info["skills"][0])  # Accessing the first skill
info["experience"] = 5  # Adding a new key-value pair
print("Updated User Information:", info)

new_info = {}
new_info = info
print("New User Information:", new_info)


nested_info = {
    "personal_info": {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    },
    "professional_info": {
        "occupation": "Software Engineer",
        "skills": {
            "primary": "Python",
            "secondary": "JavaScript"
        },
        "experience": 5
    },
}

pairs =list(nested_info["personal_info"].items())
print("before Pairs:", pairs)
pairs[0] = ("name", "Jane Smith")               #whats happen here
print("\nafter Pairs:", pairs)

print(nested_info["passord"])
print(nested_info.get("personal_info"))


new_dict = {"event": "Conference", "location": "New York", "date": {"year": 2023, "month": 10, "day": 15}}
nested_info.update(new_dict)
print("Updated Nested Info:", nested_info)

print("\nKeys:", list(nested_info.keys()))



# ============================================================================?
# PRACTICE QUESTIONS
# ===============================================


simple_dict = {
    "table": ["A piece of paper cannot decide my future, but I can.", "I am the master of my fate, the captain of my soul."],
    "cat": "a small animals that is often kept as a pet and is known for catching mice.",
}

# print("Simple Dictionary:", simple_dict)