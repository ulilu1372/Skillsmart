def UFO(N, data, octal):
    spisok = []
    if octal == True:
        for i in range(len(data)):
            spisok.append(int((str(data[i])), 8))
    if octal == False:
        for i in range(len(data)):
            spisok.append(int((str(data[i])), 16))    
    return spisok
