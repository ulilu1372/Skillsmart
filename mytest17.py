def LineAnalysis(string_line):
    sum = 0 
    for i in range(len(string_line)):
        if string_line[i] == '*':
            sum += 1
    if sum == len(string_line):
        return True
   
    if string_line[0] != '*' or string_line[len(string_line) - 1] != '*':
        return False
        
    for i in range(2, len(string_line)):
        if string_line[i] == '*':
            pattern = string_line[:i]
            break
    
    
    
    string_line = string_line[:len(string_line) - 1]
    summ = 0
    while len(string_line) != 0:
        summ += 1
        if string_line[:len(pattern)] == pattern:
            string_line = string_line[len(pattern):]
        if summ > 50:
            return False
        
    return True
        
 
            
