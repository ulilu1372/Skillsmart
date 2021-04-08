def UFO(N, data, octal):
    data = [1234,1777]
    spisok = []
    if octal == True:
        for i in range(len(data)):
            spisok.append(int((str(data[i])), 8))
    if octal == False:
        for i in range(len(data)):
            spisok.append(int((str(data[i])), 16))    
    return spisok
