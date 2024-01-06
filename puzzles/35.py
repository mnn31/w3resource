

def prod_odd_35(num):
    num_li = list(num)
    prod = 1
    for digit in num_li:
        if int(digit) % 2 != 0:
            prod *= int(digit)
    return prod
    
### MAIN PROGRAM
##35
while True:
    num = input("Number: ")
    print(f'The product of all odd numbers in {num} is {prod_odd_35(num)}')

