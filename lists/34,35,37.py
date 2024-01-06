#34,35,37

def get_prime_34(limit):
    li = list()
    for num in range(2, int(limit) + 1):
        li.append(num)
    for num in li:
        for check_num in li:
            if num == check_num:
                continue
            elif check_num % num == 0:
                li.remove(check_num)
    return li


def prod_odd_35(num):
    num_li = list(num)
    prod = 1
    for digit in num_li:
        if int(digit) % 2 != 0:
            prod *= int(digit)
    return prod
    
### MAIN PROGRAM
## 34
inp = input("Max number: ")
print(get_prime_34(inp))

##35
num = input("Number: ")
print(f'The product of all odd numbers in {num} is {prod_odd_35(num)}')

