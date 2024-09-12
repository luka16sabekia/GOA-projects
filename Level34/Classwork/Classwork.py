# 1
# NameError: ეს შეცდომა ჩნდება მაშინ, როდესაც ცვლადს ან ფუნქციას ვიყენებთ, რომელიც არ არის განსაზღვრული ან არ არის ხელმისაწვდომი.

# IndexError: ეს შეცდომა ჩნდება, როდესაც სიის, ლისტის ან სხვა კოლექციის იმ ინდექსს მივმართავთ, რომელიც მის ფარგლებს გარეთ არის.

# ValueError: ეს შეცდომა ჩნდება მაშინ, როდესაც ფუნქცია ან ოპერაცია იღებს სწორ ტიპის არგუმენტს
# მაგრამ არგუმენტის მნიშვნელობა არასწორია ან მისთვის მიუღებელია.

# TypeError: ეს შეცდომა ჩნდება მაშინ, როდესაც ოპერაცია ან 
# ფუნქცია მიიღებს არგუმენტს არასწორი ტიპის ან არაპასიხდება მათ ტიპებს შორის მოქმედებას



# 2
try:
    print()  
except NameError:
    print("NameError: ცვლადი არ არის განსაზღვრული.")


# 3
my_list = [1, 2, 3]
try:
    print(my_list[5])  
except IndexError:
    print("IndexError: ინდექსი არ არის სიის ფარგლებში.")


# 4

try:
    number = int("abc") 
except ValueError:
    print("ValueError: არასწორი მნიშვნელობა რიცხვში კონვერტაციისთვის.")