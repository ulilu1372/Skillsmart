def odometer(oksana):
    a = 0
    b = 0
    c = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            a = list[i]
        if i % 2 != 0 and i != 1:
            b = oksana[i] - oksana[i - 2]
            c += a * b
        if i == 1:
            b = oksana[i]
            c += a * b         
    return c
