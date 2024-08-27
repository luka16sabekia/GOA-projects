#2) შექმენით dictionary 3 key:value წყვილით და for loopის დახმარებით გამოიტანეთ key,
#  value ასეთი ფორმატით "Key: {key}, Value: {value}" (დაგჭირდებათ .items() მეთოდი)
key = {
    "name": "luka",
    "age": 15,
    "city": "Tbilisi"
}

for key, value in key.items():
    print(f"Key: {key}, Value: {value}")
