import random
import math


def create_perms(orig):
    perms = set()
    perms.add(', '.join(orig))
    count = 0
    fact_len = math.factorial(len(orig))
    while len(perms) != fact_len:
        random.shuffle(orig)
        perms.add(', '.join(orig))
        count += 1
    return perms, count


##### MAIN ######
while True:
    orig_li = input("Enter numbers seperated by commas: ").split(',')
    set_of_perms, count = create_perms(orig_li)
    n = 1
    for perm in set_of_perms:
        print(perm)
        n += 1
    print(f'It took {count} tries to get {n-1} perms')