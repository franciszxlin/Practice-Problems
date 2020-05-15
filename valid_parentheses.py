# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:14:47 2020

@author: Francis Lin
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

def is_valid_parenthese(s): 
    s, stack = list(s), [0]
    while s: 
        brkt = s.pop()
        if brkt == '(':
            if stack[-1] == ')': stack.pop()
            else: stack.append(brkt)
        elif brkt == '[': 
            if stack[-1] == ']': stack.pop()
            else: stack.append(brkt)
        elif brkt == '{': 
            if stack[-1] == '}': stack.pop()
            else: stack.append(brkt)
        else: stack.append(brkt)
    return stack[-1] == 0 

def main():
    paran = "([)]"
    print('Output : {}'.format(is_valid_parenthese(paran)))

if __name__ == '__main__': 
    main()


