age = int(input("Enter your age: "))


# if age > 60:
#     print("You are a senior")
# elif age >= 18:
#     # Block of code
#     print("You are an adult!")
#     print("This is next line")
#     print("-" * 10)
# else:
#     print("You are a minor!")



# if age >= 18 and age <= 60:
if 18 <= age <= 60:
    # Block of code
    print("You are an adult!")
    print("This is next line")
    print("-" * 10)
elif age > 60:
    print("You are a senior")
else:
    print("You are a minor!")

