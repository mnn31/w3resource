def create_list_1d(n, st):
    li = [st]*n
    return li

def create_list_2d(m, n, st):
    li = [''] * m
    l1 = create_list_1d(n, st)
    for i in range(m):
        li[i] = list(l1)

    return li

def create_list_3d(p, m, n, st):
    li = [''] * p
    l1 = create_list_2d(m, n, st)
    for i in range(p):
        li[i] = list(l1)

    return li

def create_list_3d_2(p, m, n, st):
    arr = [''] * p
    for i in range(p):
        arr[i] = [''] * m
        for j in range(m):
            arr[i][j] = [''] * n 
            for k in range(n):
                arr[i][j][k] = st

    return arr    


l = create_list_3d_2(3, 4, 6, "*")
print(l)

l1 = [i for i in range(10)]
print(l1)