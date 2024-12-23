class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                return i
            
#Time Complexity - O(n^2)
#Space Complexity - O(1)
