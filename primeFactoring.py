#!/usr/bin/env python

""" http://databasefaq.com/index.php/answer/158935/python-recursion-prime-factoring-python-recursive-solution-for-prime-factorization-duplicate"""
import time
start = time.time()

""" Iterative way """
def primeFac(n):
    lst = []
    c = 2
    while c <= n:
        if n % c == 0:
            n //= c
            lst.append(c)
        else:
            c += 1
    return lst
#print(primeFac(600851475143))

""" Recursive way """
def primeFacRecurse(n):
    lst = []
    c = 2
    if n <= c:
        lst.append(n)
    else:
        while n % c != 0:
            c += 1
        if n == c:
            lst.append(n)
        else:
            lst.append(c)
            lst += primeFac(n // c)
        return lst
print(primeFacRecurse(600851475143))
end = time.time()
print(end - start)
