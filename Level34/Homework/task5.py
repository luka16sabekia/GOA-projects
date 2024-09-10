def sum_numbers(lst):
    total = sum(int(x) for x in lst if str(x).isdigit())
    return total

print(sum_numbers([10, "10", "5", 20, "abc", "30"]))  
print(sum_numbers(["100", 200, "three", 50]))         
