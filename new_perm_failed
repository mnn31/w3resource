def print_new_perm(li):
    perm = str(li[-1]) + ''.join(li[:-1])
    return("Final perm:", ','.join(perm))

def cycle(inp):
    li = inp.split(',')
    print('The list is', li)
    for x in range(5):
        prev = print_new_perm(li)
        print('The original list was', li,'and the permutation is', print_new_perm(prev))
        x+=1
    exit




##### MAIN PROGRAM ####
st = input("Enter nums seperated by a comma: ")
cycle(st)