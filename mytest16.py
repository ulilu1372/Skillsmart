def MaximumDiscount(N, price):
    price = sorted(price, reverse = True)
    price2 = price[2::3]
    return sum(price2)
