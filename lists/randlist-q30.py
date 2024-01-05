##### Random selection from list ####
from random import randint

def get_rand(li):
    lucky_index = randint(0, len(li) - 1)
    return li[lucky_index]

def get_vals(li, last_ele_index):
    ele_count = dict()
    if last_ele_index >= len(li):
        last_ele_index = len(li)
    for ele in li[:last_ele_index]:
        if ele not in ele_count:
            ele_count[ele] = 1
        else:
            ele_count[ele] += 1
    return ele_count


#### MAIN PROGAM GUYS ####
li = input("List: ").split(',')

## random index
print(f'The lucky element is {get_rand(li)}!')

## number of elements in specified range
n = int(input("Till which index should I be checking the frequency of elements? "))
lookup = get_vals(li, n)
for ele in lookup:
    print(f'{ele} occurs {lookup[ele]} times within the specified range')