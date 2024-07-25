# task9
for i in range(1, 11):
    print(i)



# task10
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)

# task11
string = "Hello World!"
for char in string:
    print(char)

# task12
i = 1
while i <= 10:
    print(i)
    i += 1


# task13
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1


# task14
sum = 0
i = 1
while sum < 50:
    sum += i
    print("Current number:", i, "Current sum:", sum)
    i += 1
