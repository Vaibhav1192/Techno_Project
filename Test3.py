class RestrictedNumber:
    def __init__(self, value, min_val=0, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.value = value  # Calls the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not (self.min_val <= new_value <= self.max_val):
            raise ValueError(f"Value must be between {self.min_val} and {self.max_val}")
        self._value = new_value

# Example Usage
num = RestrictedNumber(50, 10, 60)  # Works
#num.value = 100
print(num.value ) # Works
#print(num)
#num.value = 100  # Raises ValueError
#print(num = RestrictedNumber(50, 10, 60))

'''
class RestrictMeta(type):
    def __new__(cls, name, bases, class_dict):
        if 'value' in class_dict and not (0 <= class_dict['value'] <= 100):
            raise ValueError("Class variable 'value' must be between 0 and 100")
        return super().__new__(cls, name, bases, class_dict)

class MyRestrictedClass(metaclass=RestrictMeta):
    value = 50  # Works
'''

a = '1'
b = '2'
print(int(a)+int(b))

class RestrictedNumber:
    def __init__(self, number):
        self._number = None
        self.number = number  # Use the property setter

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value < 0 or value > 100:
            raise ValueError("Number must be between 0 and 100")
        self._number = value

# Usage
try:
    r = RestrictedNumber(50)
    print(r.number)  # Output: 50
    r.number = 150   # Raises ValueError
except ValueError as e:
    print(e)         # Output: Number must be between 0 and 100
