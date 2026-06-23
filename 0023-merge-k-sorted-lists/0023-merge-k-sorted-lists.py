# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst=[]
        for l in lists:
            while l:
                lst.append(l.val)
                l=l.next
        lst.sort()
        dumb=ListNode()
        current=dumb
        for i in lst:
            current.next=ListNode(i)
            current=current.next
        return dumb.next