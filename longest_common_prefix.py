# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:30:49 2020

@author: Francis Lin
"""

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

def longest_common_prefix(strs):
    ans = ""
    if len(strs) == 0: return ans
    for i, j in enumerate(zip(*strs)):
        if len(set(j)) == 1: 
            ans += set(j).pop()
        else: break
    return ans

def main():
    strs = ["flower","flow","flight"]
    prefix = longest_common_prefix(strs)
    print('Output : {}'.format(prefix))

if __name__ == '__main__': 
    main()
