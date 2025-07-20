# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

       
# Time Complexity: O(n)
# Space Complexity: O(1)
# Algorithm: Two Pointer Technique (Floyd's Tortoise and Hare)