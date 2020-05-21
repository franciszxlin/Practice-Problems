# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:25:13 2020

@author: Francis Lin
"""

"""
Write a function that computes the n-th Fibonacci number. 
0, 1, 1, 2, 3, 5, 8, 13, 21...
"""

def fib_recursive(n): 
    if (n == 0) | (n == 1): return n
    else: return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n): 
    if (n == 0) | (n == 1): return n
    prev, last, temp = 0, 1, 0 
    for i in range(2, n + 1): 
        temp = last
        last += prev
        prev = temp
    return last

def fib_tail_recursive(n, prev = 0, last = 1):
    if n == 0: return prev 
    elif n == 1: return last
    else: return fib_tail_recursive(n-1, last, prev + last)

def main(): 
    pos = 8
    #ans = fib_recursive(pos)
    #ans = fib_iterative(pos)
    ans = fib_tail_recursive(pos)
    # Expect to see 21
    print('The {}th Fibonacci number is {}'.format(pos, ans))
    
if __name__ == '__main__': 
    main() 