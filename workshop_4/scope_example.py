
def my_function():
    # global x
    x = 0
    x += 1
    print(f"Inside function: x = {x}")

x = 7
my_function()
my_function()
my_function()
print(x)
