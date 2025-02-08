#from collections import Counter
'''
def encode_string(s):
    encoded = []
    count = Counter(s)
    for char in sorted(count.keys(), key=lambda x: s.index(x)):
        encoded.append(f"{char}{count[char]}")
    return "".join(encoded)

S = "pppuuuunne"
output = encode_string(S)
print(output)  # Output: p3u4n2e1
'''

#Another approach

def encode_string(s):
    encoded = []
    prev_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append(f"{prev_char}{count}")
            prev_char = char
            count = 1
    
    encoded.append(f"{prev_char}{count}")
    return "".join(encoded)

S = "pppuuuunne"
output = encode_string(S)
print(output)  # Output: p3u4n2e1


#from collections import Counter
'''
def count_occurrences(arr):
    return dict(Counter(arr))

# Example usage
Input = [3, 4, 3, 5, 3, 6]
output = count_occurrences(Input)
print(output)

'''

def split_list(lst, split_value):
    return [lst[i:i + split_value] for i in range(0, len(lst), split_value)]

# Example usage
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Split_Value = 5

rslt = split_list(List1, Split_Value)
#output = set(rslt)
print(rslt)

def split_set(s, split_value):
    lst = sorted(s)  # Convert set to sorted list to maintain order
    return {frozenset(lst[i:i + split_value]) for i in range(0, len(lst), split_value)}

# Example usage
List1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # Input as a set
Split_Value = 3

output = split_set(List1, Split_Value)
print(output)

import pandas as pd

# Sample data
data = {
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Product_ID': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [100, 150, 120, 180, 130, 200]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Pivot the table
df_pivot = df.pivot(index='Month', columns='Product_ID', values='Sales')

# Reset index (optional, depends on preferred format)
df_pivot = df_pivot.reset_index()

# Display the result
print(df_pivot)

