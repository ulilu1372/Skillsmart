def MadMax(N, Tele):
    a = sorted(Tele)[:len(Tele)//2]
    b = sorted(Tele, reverse=True)[1 : len(Tele)//2 + 1]
    c = sorted(Tele, reverse=True)[0]
    a.append(int(c))
    return a + b
