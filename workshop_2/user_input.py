name = input("What's your name? ")
age = int(input("Age? "))
is_student = input("Are you a student? ").lower() == "yes"


print(f"Name: {name}")
print(f"Age: {age}")
print(f"Student: {is_student}")

print(type(name)) # str
print(type(age)) # int
print(type(is_student)) # str