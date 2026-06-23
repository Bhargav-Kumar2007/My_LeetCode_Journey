# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=ListNode()
        current=x
        while head:
            if head.next:
                current.next=ListNode(head.next.val)
                current=current.next
                current.next=ListNode(head.val)
                current=current.next
                head=head.next.next
            else:
                current.next=ListNode(head.val)
                current=current.next
                head=head.next
        return x.next
        