#!/usr/bin/python3
"""calculating
"""
 
def minOperations(n):
    if n == 1:
        return 0
    
    num1 = 0
    num2 = 2

    while n> 1:
        if n % num2 ==0:
            n //= num2
            num1 += num2
        else:
            num2 +=1
    return num1