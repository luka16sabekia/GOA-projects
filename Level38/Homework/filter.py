# 1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

# 2


words = ['Apple', 'banana', 'Apricot', 'Cherry', 'avocado']

words_with_A = list(filter(lambda x: x.lower().startswith('a'), words))
print(words_with_A) 


# 3


numbers = [-5, -1, 0, 3, 9, -8]

positive_numbers = list(filter(lambda x: x >= 0, numbers))
print(positive_numbers)  
