try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Cannot divide by zero")