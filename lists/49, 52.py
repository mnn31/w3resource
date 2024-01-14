#49,52

def get_dict_from_li(li_key, li_val):
    ref = dict()
    for i in range(len(li_key)):
        ref[li_key[i]] = li_val[i]
    return ref

def get_dict_from_lists_comprehension(li_key, li_val):
    return {li_key[i] : li_val[i] for i in range(len(li_key))}


def minus_li(l1, l2):
    return list(set(l1)-set(l2)), list(set(l2)-set(l1))

#### MAIN PROGRAMADOR
l1 = input('List of size n (keys): ').split(',')
l2 = input('List of size n (vals): ').split(',')
h1 = get_dict_from_li(l1,l2)
h2 = get_dict_from_lists_comprehension(l1, l2)
print('dict from li (method 1):', h1)
print('dict from li (method 2):', h2)
assert(len(h1) == len(h2))
print('diff of lists: l1-l2 and l2-l1 respectively', minus_li(l1,l2))
