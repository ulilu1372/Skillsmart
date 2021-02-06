def ConquestCampaign(N, M, L, battalion):
    counter = 1
    battalion_new = []
    list = []
    for i in range(len(battalion)):
        if i % 2 != 0:
            battalion_new.append([battalion[i - 1], battalion[i]])
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            list.append([i,j])
    if list == battalion_new:
        return 1
    while list != []:
        for i in range(len(battalion_new)):
            battalion_new.append([battalion_new[i][0] + 1, battalion_new[i][1]])
            battalion_new.append([battalion_new[i][0], battalion_new[i][1] + 1])
            battalion_new.append([battalion_new[i][0], battalion_new[i][1] - 1])
            battalion_new.append([battalion_new[i][0] - 1, battalion_new[i][1]])
        counter += 1
        for a in range(len(battalion_new)):
            if battalion_new[a] in list:
                list.remove(battalion_new[a])
    return counter
