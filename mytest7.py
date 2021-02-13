def WordSearch(n, str, subs):
    sum = 0
    s = []
    a = []
    n1 = n 
    spisok = []
    for i in range(len(str)):
        if str[i] == ' ':
            s.append(i)
    for i in range(len(s)):
        if s[i] > n:
            a.append(s[i - 1])
            n = s[i - 1] + n1
        if s[i] == n:
            a.append(s[i])
            n = s[i] + n1
            
    str = list(str)
    for i in range(len(a)):
        str[a[i]] = '\n'
    str = ''.join(str)
    a.append(len(str))
    for i in range(len(a)):
        if subs in str[sum:a[i]]:
            spisok.append(1)
            sum = a[i]
        else:
            spisok.append(0)
        
    return spisok
