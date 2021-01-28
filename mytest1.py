def squirrel(N):
    N = int(input())
    if N < 0:
        return None
    fact = 1
    for i in range (2, N + 1):
        fact = fact * i
        y = str(fact)
    return int(y[0])
