#37, 39
from time import time
def no_import_needed_37(l1, l2):
    lcommon = [ele for ele in l1 if ele in l2]
    return lcommon

def o_n_common(l1, l2):
    s2 = set(l2)
    lcommon = [ele for ele in l1 if ele in s2]
    return lcommon
    

def NO_IMPORT_NEEDED_39(li):
    return ''.join(li)


### MAIN PROGRAM Q37
#l1 = input("List 1: ").split(",")
#l2 = input("List 2: ").split(",")
n = 1000
while n <= 1e8:
    print('n = ', n)
    l1 = list(range(n))
    l2 = l1.copy()
    l2.reverse()

    st = time()
    res = o_n_common(l1, l2)
    et = time()
    dur = et-st
    print(f'It took {dur} secs')
    print("# common elements =", len(res))

    n *= 10

    ### MAIN PROGRAM Q39
    #print(f"Pokemon, Unite! {NO_IMPORT_NEEDED_39(l1)}")
