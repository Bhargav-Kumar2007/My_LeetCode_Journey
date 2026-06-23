# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current=l1
        n1=""
        while current:
            n1+=str(current.val)
            current=current.next
        n2=""
        current=l2
        while current:
            n2+=str(current.val)
            current=current.next
        n=str(int(n1[::-1])+int(n2[::-1]))[::-1]
        nl=ListNode(n[0])
        x=nl
        for i in n[1:]:
            l=ListNode(i)
            x.next=l
            x=l
        return nl
