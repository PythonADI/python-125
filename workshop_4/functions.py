names = ["Nick", "George", "Jack", "Nick"]
names2 = ["ნიკა", "გიორგი", "მარიამი", "ლევანი"]


# definition of a function
def greet_user(name):  # parameters of function
    # function body / instructions that should be executed
    print(f"Hello {name}, How is your day going?")
    

for name in names:
    greet_user(name) # function call

for name in names2:
    greet_user(name)
