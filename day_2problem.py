# Python Practice Challenge: Student Email & Grade Validator

email = input("Enter your email address: ")
score = int(input("Enter your score (0-100): "))
domain = "@school.com"
if not (email.endswith(domain) and 0 <= score <= 100):
    print("Invalid input. Please ensure your email ends with '@school.com' and your score is between 0 and 100.")
else:
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Email: {email}, Score: {score}, Grade: {grade}")



str2 = "simplestring"
print(len(str2))

print(str2[1:len(str2)])

print(str2[1:12])


print(str2.find("o"))