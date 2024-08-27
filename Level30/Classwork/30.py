# 1) შექმენით dictionary და მიანიჭეთ 3 key:value წყვილი, შემდეგ კი ყველა key'ს
#  დახმარებით გამოიტანეთ ყველა value, მეთოდითაც და მეთოდის გარეშეც
key = {
    'name': 'apple',
    'age': 15,
    'city': 'New York'
}


print(key['name'])  
print(key['age'])  
print(key['city'])  


values = key.values()  
for value in values:
    print(value) 


# 2) შექმენით dictionary 3 key:value წყვილით და for loopის დახმარებით გამოიტანეთ ყველა value

key1 = {
    'name': 'samsung',
    'age': 24,
    'city': 'New York'
}

for key in key1:
    print(key1[key])


# 3) შექმენით dictionary რომლის value'ები იქნება list'ები


key2 = {
    'fruits': ['apple', 'samsung'],
    'numbers': [1, 2, 3, 4, 5],
    'colors': ['red', 'green', 'blue']
}
for key, value in key2.items():
    print(f"{key}: {value}")


# 4) შექმენით dictionary რომლის ერთ ერთი value იქნება ისევ dictionary
key3 = {
    'name': 'luka',
    'age': 15,
    'address': {
        'city': 'tbilisi',
    }
}

for key, value in key3.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")
