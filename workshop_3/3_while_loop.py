# Workshop 3 - while loop

# ==============================
# Basic while loop
# ==============================

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1


# ==============================
# while loop with user input
# ==============================

password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted!")
