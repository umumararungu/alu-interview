#!/usr/bin/python3
"""calculating
"""
 
def minOperations(n):
    if n == 1:
        return 0
    
    num = [float('inf')] * (n + 1)
    
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                num[i] = min(num[i], num[j] + i // j)
    
    return num[n] if num[n] != float('inf') else 0