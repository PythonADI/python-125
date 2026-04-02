# find the way to make user enter their password hidden
password = input("password: ")
confirm_password = input("confirm: ")

# is_correct = password == confirm_password and len(password) > 8 and not password.islower() and not password.isupper() and password.isalnum()
# print(f"მოკლე კოდი პასუხი: {is_correct}")

is_correct = True


# if password == confirm_password:
#     if len(password) > 8:
#         if not password.isupper():
#             if not password.islower():
#                 if password.isalnum():
#                     print("Password is correct")
#                 else:
#                     print("You cannot use special characters")
#             else:
#                 print("You need at least 1 upper case character")
#         else:
#             print("You need at least 1 lower case character")
#     else:
#         print("Password Should be at least 8 characters")
# else:
#     print("Passwords are not same!")




if password != confirm_password:
    print("Passwords are not same!")
    is_correct = False


if len(password) < 8:
    print("Password Should be at least 8 characters")
    is_correct = False

if password.isupper():
    print("You need at least 1 lower case character")
    is_correct = False


if password.islower():
    print("You need at least 1 upper case character")
    is_correct = False


if not password.isalnum():
    print("You cannot use special characters")
    is_correct = False


if is_correct:
    print("Password is correct")
    print("Save to Database")
else:
    print("Failed to create password")
    print("Please fix all issues")
# print(password.isupper())
# print(password.islower())
# print(password.isalnum())
