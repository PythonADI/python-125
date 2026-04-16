CORRECT_PASSWORD = "python123"
attempts = 0
is_correct = False


while attempts < 3:
    attempts += 1
    password = input("Enter password: ")
    is_correct = password == CORRECT_PASSWORD

    if not is_correct:
        print("Wrong password")
        continue

    print("Welcome")
    break

if attempts == 3 and not is_correct:
    print("Account Locked!")


