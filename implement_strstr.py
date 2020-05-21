# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:11:26 2020

@author: Francis Lin
"""

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

def str_str(haystack, needle):
    if needle == '': return 0
    for i in range(len(haystack) - len(needle) + 1): 
        if haystack[i : i + len(needle)] == needle: return i
    return -1
    
def main(): 
    a, b= 'apples', 'le'
    ans = str_str(a, b)
    # Expect to see 3
    print('Output : {}'.format(ans))

if __name__ == '__main__':
    main()

