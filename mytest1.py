def squirrel(N):
    fact = 1
    for i in range (2, N + 1):
        fact = fact * i
    y = str(fact)
    return int(y[0])
