
# task1
def manual_min(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    min_number = numbers[0]
    
    for number in numbers:
        if number < min_number:
            min_number = number
    
    return min_number

numbers = [16, 21, 18, 9, 10, 12]

print(manual_min(numbers))


# task2
def manual_max(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    max_number = numbers[0]
    
    for number in numbers:
        if number > max_number:
            max_number = number
    
    return max_number

numbers = [5, 9, 15, 17, 14, 12]

print(manual_max(numbers))

# task3
def manual_len(lst):

    count = 0

    for _ in lst:
        count += 1
    
    return count

numbers = [15, 23, 11, 40, 37, 33]

print( manual_len(numbers))

# task4
def manual_sum(numbers):
    total = 0
    
    for number in numbers:
        total += number
    
    return total

numbers = [2, 6, 22, 29, 23, 21]

print( manual_sum(numbers))


# task5
def manual_replace(s, old, new):
    result = ""
    i = 0
    
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    
    return result

text = "hello world"
old_substring = "world"
new_substring = "GOA"

print( manual_replace(text, old_substring, new_substring))

# task6
def manual_find(s, substring):
    for i in range(len(s) - len(substring) + 1):
        
        if s[i:i+len(substring)] == substring:
            return i
    return -1

text = "hello world"
substring = "world"

print(manual_find(text, substring))
