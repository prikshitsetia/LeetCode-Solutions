# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        li=ListNode()
        li2=li
        car=0
        while l1!= None and l2!=None:
            if l1.val+l2.val+car>9:
                li.val=int((l1.val+l2.val+car)%10)
                car=int((l1.val+l2.val+car)/10)
            else:
                li.val=l1.val+l2.val+car
                car=0
            l1=l1.next
            l2=l2.next
            if l1!=None or l2!=None:
                li.next=ListNode()
                li=li.next
            if l1==None and l2==None and car!=0:
                li.next=ListNode()
                li=li.next
                li.val=car
        if l1==None and l2!=None:
            while l2!=None:
                if l2.val+car>9:
                    li.val=int((l2.val+car)%10)
                    car=int((l2.val+car)/10)
                else:
                    li.val=l2.val+car
                    car=0
                l2=l2.next
                if l2!=None:
                    li.next=ListNode()
                    li=li.next
                if l2==None and car!=0:
                    li.next=ListNode()
                    li=li.next
                    li.val=car
        if l2==None and l1!=None:
            while l1!=None:
                if l1.val+car>9:
                    li.val=int((l1.val+car)%10)
                    car=int((l1.val+car)/10)
                else:
                    li.val=l1.val+car
                    car=0
                l1=l1.next
                if l1!=None:
                    li.next=ListNode()
                    li=li.next
                if l1==None and car!=0:
                    li.next=ListNode()
                    li=li.next
                    li.val=car
        #li=None
        return li2
            
            
        