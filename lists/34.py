#34
from time import time


def get_prime_34(limit):

    li = [i for i in range(2, limit+1)]
    for i in range(len(li)):
        num = li[i]
        if num == '*': continue
        for check_indx in range(num*num-2, len(li), num):
            li[check_indx] = '*'

    res = [ele for ele in li if ele != '*']        

    
    return res

    
### MAIN PROGRAM
## 34
while True:
    inp = int(input("Max number: "))

    st = time()
    res = get_prime_34(inp)
    et = time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print('Found primes:', len(res))
    print(res)
