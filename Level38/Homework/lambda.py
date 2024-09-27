# 1


tuples_list = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list) 

# 2

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print(squares)  

# 3

words = ['apple', 'cat', 'banana', 'dog', 'ant']

filtered_words = list(filter(lambda x: len(x) < 4, words))
print(filtered_words)  