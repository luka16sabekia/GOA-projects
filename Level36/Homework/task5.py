products = {
    "ვაშლი": True,
    "ფორთოხალი": False,
    "ბანანი": True,
    "ყურძენი": False,
    "კივი": True,
    "მსხალი": False
}

out_of_stock = dict(filter(lambda item: not item[1], products.items()))

print(out_of_stock)
