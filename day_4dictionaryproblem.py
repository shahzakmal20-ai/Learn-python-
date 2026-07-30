# Scenario:
# You are maintaining a student record in a nested dictionary format.
#  You need to update grades and retrieve dictionary attributes using dictionary methods.

student = {
    "name": "Rahul",
    "subjects": {
        "phy": 85,
        "chem": 90,
        "math": [20, 30, [39, 40, 50], 60]
    }
}

student["subjects"]["math"] = 95  # Update Math grade

student["subjects"].update({"eng": 92})  # Add English grade

print("Updated Student Record:", student)

print("Number of Subjects:", len(student["subjects"]))  # Get the number of subjects

print("Top level keys:", list(student.keys()))  # Get all keys in the student dictionary

print(student["subjects"]["math"][2][2])  # Accessing the second element of the nested list within Math grades


# Problem2 Scenario:
# You are maintaining a student record in a nested dictionary format.
#  You need to update grades and retrieve dictionary attributes using dictionary methods.

profile_basic = {
    "id": 101,
    "name": "Ananya",
    "role": "Developer"
}

profile_extra = {
    "department": "Engineering",
    "salary": 75000
}


print("Experience value:",profile_basic.get("experience"))  # Accessing the value of "experience" key using get method

profile_basic.update(profile_extra)  # Merging profile_extra into profile_basic
print("Merged Profile:", profile_basic)

print("All items in profile_basic:", list(profile_basic.items()))  # Getting all keys in profile_basic