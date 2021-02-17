def WordSearch(n, str, subs):
    sum = 0
    sum1 = 0
    s = []
    a = []
    n1 = n 
    spisok = []
    if ' ' not in str:
            for i in range(len(str)):
                if i == n:
                    str = str[:i] + '\n' + str[i:]
                    a.append(i)
                    n = n + n1
                if i != n:
                    sum1 += 1
                  
                if sum1 == len(str):
                    return [0]
              
            for i in range(len(a)):
                if subs in str[sum:a[i]]:
                    spisok.append(1)
                    sum = a[i]
                else:
                    spisok.append(0)
            for i in range(len(a)):
                if subs in str[sum:a[i]]:
                    spisok.append(1)
                    sum = a[i]
                else:
                    spisok.append(0)
            
            return spisok
            
    elif ' ' in str:                        
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
    else:
        return [0]
