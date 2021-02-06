def SynchronizingTables(N,  ids, salary):
    salary_true = []
    ids_copy = sorted(ids)
    salary_copy = sorted(salary)
    for i in ids:
        for j in range(len(ids_copy)):
            if i == ids_copy[j]:
                salary_true.append(salary_copy[j])
    return salary_true
