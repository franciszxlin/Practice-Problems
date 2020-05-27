# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:04:13 2020

@author: Francis Lin
"""

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

# Solution utilizes Kadane's algorithm.
def max_sub_array(nums): 
    max_ending_here, max_so_far = nums[0], nums[0] 
    for num in nums[1:]:  
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main():
    array = [-2, -3, 4, -1, -2, 1, 5, -3] # Expect to see 7
    #array = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # Expect to see 6
    ans = max_sub_array(array)
    print('Output : {}'.format(ans))

if __name__ == '__main__': 
    main()
    

