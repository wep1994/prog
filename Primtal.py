__author__ = 'sebsyv'
# boolean operators are not, and, or

#!/bin/python

[0, 1]


def is_prime(integer):
    """Determines weather integer is prime, returns a boolean value"""
    # add logic here to make sure number < 2 are not prime

    if integer in [0, 1]:
     return False

    for i in range(2, integer):
       if integer % i == 0:
            return False
    return True


for i in range(5000):
    if is_prime(i) == True:

        print i, "is a prime number"

#print("Should be False (0): %r" % is_prime(0))
#print("Should be False (1): %r" % is_prime(1))
#print("Should be True  (2): %r" % is_prime(2))
#print("Should be False (8): %r" % is_prime(8))
#print("Should be True (17): %r"% is_prime(17))


# Your code below:
