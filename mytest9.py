def StringRabbitsFoot(s, encode):
    if encode == True:
        new_s = s.replace(' ', '')
        l = len(new_s)
        matrix = []
        new_matrix = []
        sqrt = l ** 0.5
        rows = int(sqrt)
        columns = round(sqrt)
        while l > rows * columns:
            rows += 1
        for x in range(0, len(new_s), columns):
            matrix.append(new_s[x:x+columns])
        for i in range(columns):       
            if i == len(matrix[rows - 1]) - 1:
                for j in range(rows):
                    new_matrix.append(matrix[j][i])
                new_matrix.append(' ')
            else: 
             for j in range(rows - 1):
                new_matrix.append(matrix[j][i])
             new_matrix.append(' ')
        new_matrix = ''.join(new_matrix)
        return new_matrix

    if encode == False:
        new_matrix = s
        length = len(new_matrix.replace(" ", ""))
        new_matrix = new_matrix.split()
        spisok = []
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix)):
                spisok.append(new_matrix[j][i])
                if len(spisok) == length:
                    break
        spisok = ''.join(spisok)
        
        return spisok
