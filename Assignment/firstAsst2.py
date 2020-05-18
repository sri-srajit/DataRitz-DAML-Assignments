# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:34:08 2020

@author: Srajit Srivastava
"""
def armstrong(n):
    sum = 0
    N = n
    while(n):
        d = n%10
        sum += d**3
        n = n//10
    if(sum == N):
        return True
    return False
n = int(input("Enter a number "))
if(armstrong(n)):
    print("Number is Armstrong Number")
else:
    print("Number is not Armstrong Number")