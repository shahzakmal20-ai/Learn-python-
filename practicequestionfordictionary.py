wordsmeaning = {
    "table" : ["a peice of paper", "list of facts and figures"],
    "cat" : "a small animal"
}
print(wordsmeaning)

print(wordsmeaning["table"])
print(wordsmeaning["cat"])

# program to add marks of 3 subjects in dictionary takes marks from user

marks = {}
sub1 = int(input("enter the marks of First subject: "))
marks["english"] = sub1
sub2 = int(input("enter the marks of second subject: "))
marks["maths"] = sub2
sub3 = int(input("enter the marks of third subject: "))
marks["computer"] = sub3
print(marks)