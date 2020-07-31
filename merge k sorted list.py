# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,l1,l2):
        if l1==None and l2==None:
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1
        if l1.val<=l2.val:
            l1.next=self.merge(l1.next,l2)
        else:
            temp=ListNode(l2.val,None)
            temp.next=l1
            l1=temp
            l1.next=self.merge(l1.next,l2.next)
        return l1

    def mergeKLists(self, lists: List[ListNode]):
        if len(lists)==0:
            return
        elif len(lists)==1:
            return lists[0]
        l=len(lists)
        interval=1
        while interval<l:
            for i in range(0,l-interval,interval*2):
                lists[i]=self.merge(lists[i],lists[i+interval])
            interval*=2
        return lists[0]