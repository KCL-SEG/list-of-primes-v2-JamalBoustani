"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes<1):
        raise ValueError("0 and negative numbers not accepted")
    list = []
    count = 0
    prime_number = 2
    while count < number_of_primes:
        for n in range(2,prime_number):
            if(prime_number % n == 0):
                break
        else:   
            list.append(prime_number)
            count+=1
            
        
        prime_number += 1

    return list
