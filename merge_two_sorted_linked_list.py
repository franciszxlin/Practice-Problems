# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:24:16 2020

@author: Francis Lin
"""

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def merge_two_lists(l1, l2):
    head = ListNode()
    ptr = head
    while True: 
        if (l1 is None) & (l2 is None): break
        elif l1 is None:
            ptr.next = l2
            break 
        elif l2 is None:
            ptr.next = l1
            break
        else: 
            smaller = 0
            if l1.val < l2.val: 
                smaller = l1.val
                l1 = l1.next
            else: 
                smaller = l2.val
                l2 = l2.next
            newNode = ListNode(smaller)
            ptr.next = newNode
            ptr = ptr.next
    return head.next


