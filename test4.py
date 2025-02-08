class Base: 
    def __init__(self, a = 1): 
        self.a = a 

class Derived(Base): 
    def __init__(self, b = 2): 
        super().__init__() 
        self.b = b

def main(): 
    obj = Derived() 
    print(obj.a, obj.b) 

main()

d = {i: i*i for i in range(10)}

print(d)
# Second Highest no. from list without Builtin function
lst = [1, 2, 4, 10, 18]
lrg = float('-inf')
snd_lrg = float('-inf')

for num in lst:
    if num > lrg:
        snd_lrg = lrg
        lrg = num
    elif num > snd_lrg and num  != lrg:
        snd_lrg = num
print('Second highest number is :',snd_lrg)
    
# Find Indices from above list of elements whose sum is 13. 
target_sum = 15

def find_indice(lst, target_sum):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return i, j ,k
    return None
    
indices = find_indice(lst, target_sum)

if indices:
    print('Indices of elements whose sum of 13:',indices)
else:
    print("No pairs of elements found whose sum of 13.")

import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)

# Modifying the nested list
shallow_copy[1][0] = 'ddhh'
print(original_list)  # Output: [1, ['changed', 3], 4]
print(shallow_copy)   # Output: [1, ['changed', 3], 4]

#Find and Grape
T = 'Hello world of Python'
ind = T.find('Python')
print(ind)


list = [7,3,5,6,7,8]
max = list[0]
for x in list:
    if x > max:
        max = x
print( max)

min = list[0]
for x in list:
    if x < min:
        min = x
print( min)