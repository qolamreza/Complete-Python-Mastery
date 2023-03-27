message = "a"


def greet(name):
    global message
    message = "b"


greet("Reza")
print(message)