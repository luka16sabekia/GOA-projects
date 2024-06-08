"""5) შექმენით 2 ცვლადი num1 და num2. მათი მნიშვნელობები შემოატანინეთ მომხმარებელს და შეადარეთ,
num1 მეტია თუ არა num2'ზე, num1 ნაკლებია თუ არა num2'ზე და num1 ტოლია თუ არა num2'ის.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


more_than = num1 > num2  
less_than = num1 < num2     
equal_to = num1 == num2 


print(f"First number is greater than second number: {more_than}")  
print(f"First number is lower than second number: {less_than}")  
print(f"First number equal to second number: {equal_to}")  