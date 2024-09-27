# 1


strings = ['hello', 'world', 'python']

uppercase_strings = list(map(lambda x: x.upper(), strings))
print(uppercase_strings)  

# 2


numbers = [10, 20, 30, 40]

updated_numbers = list(map(lambda x: x + 5, numbers))
print(updated_numbers)  

# 3


words = ['apple', 'banana', 'cherry']

modified_words = list(map(lambda x: "-start" + x[0], words))
print(modified_words)  
