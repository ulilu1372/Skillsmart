def PatternUnlock(N, hits):
    sum = 0
    for i in range(1, len(hits)):
        if hits[i] == 6 and hits[i - 1] == 2 or hits[i] == 2 and hits[i - 1] == 6:
            sum += 2**(1./2)
        elif hits[i] == 2 and hits[i - 1] == 9 or hits[i] == 9 and hits[i - 1] == 2:
            sum += 2**(1./2)
        elif hits[i] == 2 and hits[i - 1] == 4 or hits[i] == 4 and hits[i - 1] == 2:
            sum += 2**(1./2)
        elif hits[i] == 2 and hits[i - 1] == 7 or hits[i] == 7 and hits[i - 1] == 2:
            sum += 2**(1./2)
        elif hits[i] == 1 and hits[i - 1] == 5 or hits[i] == 5 and hits[i - 1] == 1:
            sum += 2**(1./2)
        elif hits[i] == 5 and hits[i - 1] == 3 or hits[i] == 3 and hits[i - 1] == 5:
            sum += 2**(1./2)
        elif hits[i] == 3 and hits[i - 1] == 8 or hits[i] == 8 and hits[i - 1] == 3:
            sum += 2**(1./2)
        elif hits[i] == 8 and hits[i - 1] == 1 or hits[i] == 1 and hits[i - 1] == 8:
            sum += 2**(1./2)
        else: 
            sum += 1
    s = list(str(int((round(sum, 5) * 100000))))
    while '0' in s:
        s.remove('0')
    s = ''.join(s)

    return s
