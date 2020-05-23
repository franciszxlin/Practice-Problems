# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:52:06 2020

@author: Francis Lin
"""

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""

def count_and_say(n): 
    string = '1'
    for i in range(n - 1):
        cnt = 0
        new_string = []
        prev_c = None
        for c in string:
            if prev_c is not None and prev_c != c:
                new_string.append(str(cnt)+prev_c)
                cnt = 0
            cnt += 1
            prev_c = c
        new_string.append(str(cnt)+c)
        string = ''.join(new_string)
    return string
    
def main(): 
    term = 6 
    ans = count_and_say(term)
    # Expect to see 312211
    print('Output : {}'.format(ans))
    
if __name__ == '__main__': 
    main()


