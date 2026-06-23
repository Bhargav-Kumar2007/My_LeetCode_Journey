# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        l=[]
        while current:
            l.append(current.val)
            current=current.next
        l.pop(-n)
        lol=ListNode()
        x=lol
        for i in l:
            x.next=ListNode(i)
            x=x.next
        return lol.next