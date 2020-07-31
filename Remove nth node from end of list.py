# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first=head
        sec=head
        for i in range(n):
            if first.next==None:
                if i==n-1:
                    head=head.next
                return head
            first=first.next
            
        while first.next!=None:
            first=first.next
            sec=sec.next
        sec.next=sec.next.next
        return head
            
            
        