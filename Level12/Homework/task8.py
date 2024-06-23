"""8) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ ფოტოს მიხედვით:
(ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით
ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)"""



score = int(input("please enter your score: "))


if 90 <= score <= 100:
    grade = "Grade A"
elif 80 <= score <= 89:
    grade = "Grade B"
elif 70 <= score <= 79:
    grade = "Grade C"
elif 60 <= score <= 69:
    grade = "Grade D"
elif 50 <= score <= 59:
    grade = "Grade E"
else:
    grade = "Grade F"

print("your Grade is:", grade)
