lists = [
    [4, 8, 12],
    [10, 20, 30],
    [5, 15, 25],
    [6, 18, 24]
]

averages = list(map(lambda x: sum(x) / len(x), lists))

print(averages)  
