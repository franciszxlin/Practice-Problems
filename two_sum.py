# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:59:39 2020

@author: Francis Lin
"""

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def two_sum(nums, target): 
    need = {}
    for i in range(len(nums)): 
        if target - nums[i] in need: 
            return [need[target - nums[i]],i]
        else:
            need[nums[i]] = i

def main():
    given = [2, 7, 11, 15]
    target = 9
    ans = two_sum(given, target)
    print('Expected: [0, 1]')
    print('Answer: {}'.format(ans))

if __name__ == '__main__': 
    main()

