# Try.....Except
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Cannot divide by zero")

finally:
    # Code that always runs, regardless of exceptions
    print("This will always execute")

# Try....Finally
try:
    a = 10
    b = 0
    result = a / b
finally:
    # Code that always runs, regardless of exceptions
    print("This will always execute")


def foo():
    try:
        return 1
    
    finally:
        return 2
K = foo()
print(K)
