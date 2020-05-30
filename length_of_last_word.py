# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:18:54 2020

@author: Francis Lin
"""

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

def length_of_last_word(s): 
    l = 0
    x = s.strip()
    for c in x: 
        if c == ' ': l = 0
        else: l += 1
    return l

def main(): 
    phrase = 'Hello World'
    ans = length_of_last_word(phrase)
    # We expect 5 here. 
    print('Output : {}'.format(ans))

if __name__ == '__main__': 
    main()