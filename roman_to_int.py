# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:47:04 2020

@author: Francis Lin
"""

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""

def roman_to_int(s):
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    ints = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
    mapping = dict(zip(romans, ints))
    i, total = 0, 0
    while i < len(s): 
        if (i + 1 < len(s)) & (s[i:i+2] in mapping):
            total += mapping[s[i:i+2]]
            i += 2
        else:
            total += mapping[s[i]]
            i += 1
    return total

def main():
    roman_numerals = 'CDXLIII'
    ans = roman_to_int(roman_numerals)
    print('Output : {}'.format(ans))
    
if __name__ == '__main__': 
    main()


