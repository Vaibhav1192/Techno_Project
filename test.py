# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper
# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper
@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'
hello()   # output => [ 'hello' , 'world' ]
print(hello())

def names_everything(function):
    def wrapper(aeg1,aeg2):
        aeg1 = aeg1.capitalize()
        aeg2 = aeg2.capitalize()
        str_hi = function(aeg1,aeg2)
        return str_hi
    return wrapper

@names_everything
def nmes(name1, name2):
    return name1 , name2
print(nmes('hi', 'vaibhav'))


T =  'Hello Python'
def str_rng(T):
    for i in range(5):
        return i
    
print(str_rng)


      

