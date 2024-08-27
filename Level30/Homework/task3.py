# 3) შექმენით 3 მანქანის dictionary (ობიექტი), ერთიდაიგივე key'ებით მაგრამ განსხვავებული value'ებით
#  და წარმოუდგინეთ მომხმარებელს, თითქოს უნდა მიყიდოთ რომელიმე მანქანა და ეუბნებით ინფორმაციას მათ შესახებ
car1 = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "price": "$15,000"
}

car2 = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2019,
    "price": "$14,000"
}

car3 = {
    "brand": "Ford",
    "model": "Focus",
    "year": 2021,
    "price": "$16,500"
}

cars = [car1, car2, car3]

for index, car in enumerate(cars, start=1):
    print(f"car {index}:")
    for key, value in car.items():
        print(f"{key.capitalize()}: {value}")
    print("\n")
