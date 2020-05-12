# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:20:49 2020

@author: Francis Lin
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.
"""
def reverse(x):
    negative = False
    if x < 0: negative, x = True, -x
    ans = 0
    while x > 0:
        ans = ans * 10 + x % 10
        x //= 10
    if(ans > (2 ** 31 - 1)): return 0 # Handle maximum 32bit number
    return -ans if negative else ans

def main():
    original_integer = 8464200
    reversed_integer = reverse(original_integer)
    print('Output : {}'.format(reversed_integer))

if __name__ == '__main__': 
    main()
