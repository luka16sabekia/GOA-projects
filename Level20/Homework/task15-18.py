# task15
def check_divisibility():
    number = int(input("Enter a number: "))
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} is divisible by both 3 and 5.")
    elif number % 3 == 0:
        print(f"{number} is divisible by 3.")
    elif number % 5 == 0:
        print(f"{number} is divisible by 5.")
    else:
        print(f"{number} is not divisible by 3 or 5.")
        
check_divisibility()



#task16
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

numbers = [43, 90, 123, 63, 32]
print("Average of [43, 90, 123, 63, 32]:", calculate_average(numbers))


#task17
def alternate_uppercase(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i]
    return result
string = "hello"
print("Output:", alternate_uppercase(string))


#task18
def square_numbers(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

numbers = [3, 12, 5, 2, 6]
print("New list:", square_numbers(numbers))
