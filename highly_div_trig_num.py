import math

def isPrime(x):
    """Check for x to be a prime number
       return True is x is prime else False"""
    for i in range(2,long(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def primeFactors(num):
    """Returns all the prime factors of a number
    """
    prime_list = {}
    factor = 2
    while not isPrime(num):
        if num%factor == 0:
            if factor in prime_list:
                prime_list[factor] += 1
            else:
                prime_list[factor] = 1
            num/=factor
        else:
            factor += 1
            while not isPrime(factor):
                factor += 1
    if num in prime_list:
        prime_list[num] += 1
    else:
        prime_list[num] = 1
    return prime_list


def numOfFact():
    """ Funtion to find first number to have more then 500 factors
    """
    i = 1
    sum = 1
    while True :
        numOfFact = 1
        prime_list = primeFactors(sum)
        for prime in prime_list:
            numOfFact *= prime_list[prime]+1
        if numOfFact >500:
            print sum,numOfFact
            break
        print sum,numOfFact
        i += 1
        sum += i
        
numOfFact()
