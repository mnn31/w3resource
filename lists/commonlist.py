def common(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return not (not s1.intersection(s2))

#### Main Program ####
l1 = input("List 1: ").split(',')
l2 = input("List 2: ").split(',')
print(common(l1, l2))
