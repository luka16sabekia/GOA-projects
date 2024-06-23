"""5) გამოიყენეთ while loop და ისევ გააკეთეთ მეორე დავალების მსგავსი თამაში. რიცხვები იქნება 1'დან 10'ის ჩათვლით
 და სანამ მომხმარებელი არ შემოიტანს სწორ რიცხვს, დაუწერეთ რომ არასწორია, თუ სწორად შემოიტანს დაუწერეთ რომ სწორია."""


answer = (10)

guess = int(input("enter number 1 to 10: "))

while guess != answer:
    print("It's incorrect")
    guess = int(input("enter number 1 to 10: "))

print("It's correct")