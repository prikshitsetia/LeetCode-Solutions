# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None:
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
        else:
            temp=ListNode(l2.val,None)
            temp.next=l1
            l1=temp
            l1.next=self.mergeTwoLists(l1.next,l2.next)
        return l1
        