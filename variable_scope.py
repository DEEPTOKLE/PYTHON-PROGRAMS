x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        y = 30
        print("Nonlocal variable:", y)

    inner()

def display():
    z = 40
    print("Local variable:", z)

display()
print("Global variable:", x)
outer()