#task1
age = int(input("Enter your age: "))

if age < 13:
    print("You are kid")
elif 13 <= age < 20:
    print("You are teenager")
else:
    print("You are grown up")

    # task2

i = 1
while i <= 100:
    if i < 40 or i > 50:
        print(i)
    i += 1