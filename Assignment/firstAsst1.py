"""
Created on Mon May 18 19:34:08 2020

@author: Srajit Srivastava
"""

def prime(n):
    size = int(n**(0.5)+1)
    for i in range (2,size):
        if(n%i == 0):
            return False
    return True
def printPrime(a,b):
    for i in range(a,b+1):
        if(prime(i)):
            print(i,end=" ")
a = 100
b = 300
printPrime(a, b)