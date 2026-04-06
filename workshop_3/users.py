users = ["Alice", "Bob", "Charlie", "david", "Eve"]

username = input("Enter username: ")

# if username in users:
#     print("Username found")
# else:
#     print("Not found!")

username_exists = False
for user in users:
    if user.lower() == username.lower():
        username_exists = True
        break

if username_exists:
    print("username found")
else:
    print("username not found")

