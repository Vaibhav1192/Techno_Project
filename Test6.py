try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Cannot divide by zero")