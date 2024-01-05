import math

def is_prime(n):
    for x in range(2, int(math.sqrt(n))+1):
        #print('testing factor', x, 'against', n)
        if n % x == 0:
            print(n, 'modulo', x,
                  'is zero so it divisible by', x)
            return False
    return True

def checkprime(li):
    for num in li:
        if not is_prime(int(num)):
            print(num, 'is not prime')
            return False
        
    return True


#### MAIN PROGRAM ############
while True:
    li = input("List of nums: ").split(',')
    print(checkprime(li))
                
