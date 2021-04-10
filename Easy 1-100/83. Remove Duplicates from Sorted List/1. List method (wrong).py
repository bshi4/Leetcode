# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# I treat head as a list but not linked list, so this method is not correct!!!
class Solution:
    def deleteDuplicates(self, head):
        head1 = []
        head1.append(head[0])
        for i in range(1, len(head)):
            if head[i] != head[i-1]:
                head1.append(head[i])
        return head1

head = [1,1,2,3]
ans = Solution().deleteDuplicates(head)
        