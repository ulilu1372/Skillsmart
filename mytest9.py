#def StringRabbitsFoot(s, encode):
encode = False
s = 'отдай мою кроличью лапку'
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
print(new_matrix)

new_matrix = 'омоюу толл дюиа акчп йрьк'
length = len(new_matrix.replace(" ", ""))
new_matrix = new_matrix.split()
spisok = []
for i in range(len(new_matrix)):
    for j in range(len(new_matrix)):
        spisok.append(new_matrix[j][i])
        if len(spisok) == length:
            break
print(''.join(spisok))
