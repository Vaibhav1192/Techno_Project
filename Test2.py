def dec_lowercase(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

def dec_splitcase(function):
    def wrapper():
        func = function()
        split_uppercase = func.split()
        return split_uppercase
    return wrapper

@dec_splitcase
@dec_lowercase

def Hello():
    return 'hello World'
print(Hello())

# *args and **Kwargs
#1)*args
def everything_show(*args):
    for count, thing in enumerate(args):
        print('{0}.{1}'.format(count,thing))
everything_show('xpulse','pulsar','shine')

#2)**Kwargs
def everything_key(**kwargs):
    for name, value in kwargs.items():
        print('{0}={1}'.format(name,value))

everything_key(name ='Vaibhav', value = 100000)

def fun(min):
    cnt = 5
    while cnt >= min:
        yield cnt
        cnt -=1

ctr = fun(1)
for n in ctr:

    print(n)

def countdwon():
    while n > 0:
        yield n
        n -=1

gen = countdwon(5)
for num in gen:
    print(num)