#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# Algorithm: Two Pointer Technique (Floyd's Tortoise and Hare)