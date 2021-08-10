def TransformTransform(A, N):
    B = []
    for i in range(N):
        for j in range(N-i):
            k = i + j
            max_number = 0
            for h in range(j, k+1):
                if max_number < A[h]:
                    max_number = A[h]
            B.append(max_number)
    # print(B)
    BB = []
    for i in range(len(B)):
        for j in range(len(B)-i):
            k = i + j
            max_number = 0
            for h in range(j, k+1):
                if max_number < B[h]:
                    max_number = B[h]
            BB.append(max_number)
    # print(BB)
    summ = 0
    for x in range(len(BB)):
        summ += BB[x]
    # print(summ)
    if summ % 2 == 0:
        return True
    else:
        return False
