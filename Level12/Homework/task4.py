"""4) გამოიყენეთ for loop'ი, გამოიტანეთ 1დან 1000'მდე
 რიცხვების ჯამი მაგრამ გამოტოვეთ რიცხვები range(500, 600)'ში (ანუ ხუთასიდან ექვსასამდე რიცხვები არ დაამატოთ)"""



sum = 0

for number in range(1, 1001):
    if 500 <= number < 600:
        continue
    sum += number


print("the sum of numbers from 1 to 1000 (excluding numbers from 500 to 600) is:", sum)
