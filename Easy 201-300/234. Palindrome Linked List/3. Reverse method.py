# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        mid = n // 2
        
        def reverse(head):
            prev = None
            while head:
                temp = head
                head = head.next
                temp.next = prev 
                prev = temp
            return prev
        
        i = 0
        first = second = head
        while i < mid:
            second = second.next
            i += 1
        second = reverse(second)
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
            
        