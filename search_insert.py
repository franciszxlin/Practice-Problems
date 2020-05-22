# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:34:39 2020

@author: Francis Lin
"""

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

def search_insert(nums, target): 
    for i, num in enumerate(nums): 
        if num >= target: return i
    return len(nums)

def main(): 
    array, tar = [1,3,5,6], 7
    ans = search_insert(array, tar)
    # Expect to see 4
    print('Output : {}'.format(ans))
    
if __name__ == '__main__': 
    main()