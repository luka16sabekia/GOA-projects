"""Extract random elements of a list with negative indexes"""
list1 = [2, 51, 11, 13, 51, 100]

elements = [list1[i] for i in [-3, -5, -2]]
print(elements)
