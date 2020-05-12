# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:32:21 2020

@author: Francis Lin
"""

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""

def is_palindrome(x):
    if x < 0: return False
    div, copy_x = 1, x
    while copy_x // div >= 10: 
        div *= 10
    while x != 0: 
        left, right = x // div, x % 10
        if left != right: return False
        x = (x - left * div) // 10 
        div //= 100
    return True

def main():
    input_number = 9283443829 # True
    ans = is_palindrome(input_number)
    print('Output : {}'.format(ans))
    
if __name__ == '__main__': 
    main()
