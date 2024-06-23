"""2) ხელახლა გააკეთეთ კლასში გაკეთებული dice roll თამაში. აიღეთ რაიმე რიცხვი 1დან 6ის ჩათვლით რაც იქნება სწორი პასუხი
. აიღეთ ასევე guess რომელსაც მომხმარებელი შემოიტანს.
 თუ სწორად გამოიცნობს დაუწერეთ "It's correct", თუ არასწორად "It's incorrect"."""


num = 3
guess = int(input("enter number 1 to 6: "))

if guess == num :
    print("It's correct")
else:
    print("It's incorrect")
