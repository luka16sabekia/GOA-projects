""" Output every item from list with negative indexing."""
list1 = [2, 51, 11, 13, 51, 100]

for i in range(-1, -len(list1) - 1, -1):
    print(list1[i])