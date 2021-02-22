def WordSearch(widht_str, s, subs):
    court = 0  
    court1 = 0  
    court_all = 0  
    court_speace = 0  
    add_str = ''
    sum_arr = []
    line_length = 0
    j = 0
    len_frases = len(s)
    for i in range(len_frases):
        while j < len(s) - 1:
            if s[court] == ' ':  
                court += 1
                court_speace = 1  
                
            for j in range(0 + court,
                           widht_str + court):  
                court_all += 1
                court1 += 1
                add_str += s[j]  
                if j == len(s) - 1:  
                    sum_arr.append(add_str)
                    break
                if widht_str == court1:
                    if add_str.find(' ') == -1 and s[(line_length + court1)] != ' ':
                        sum_arr.append(add_str)
                    if add_str.find(' ') != -1 and s[
                        (line_length + court1)] != ' ':
                        for k in range(len(add_str) - 1, -1, -1):  
                            if add_str[k] == ' ':  
                                add_str = add_str[0:k]  
                                sum_arr.append(add_str)
                                break
                    if s[(line_length + court1)] == ' ':
                        sum_arr.append(add_str)
                    line_length += len(
                        add_str) + court_speace  
                    court += len(add_str)
                    add_str = ''
                    court1 = 0
                    court_speace = 0
    end_arr = []
    for h in sum_arr:
        if subs in h.split():
            end_arr.append(1)
        else:
            end_arr.append(0)

    return end_arr
