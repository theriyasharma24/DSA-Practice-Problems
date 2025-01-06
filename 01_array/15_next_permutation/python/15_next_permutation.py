class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index=0
        n=len(nums)
        for i in range(n-1, -1, -1):
            if nums[i-1] < nums[i]:
                index = i-1
                break
        if index==-1:
            nums[:]=nums[::-1]
        else:
            for i in range(n-1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            nums[index+1:] = reversed(nums[index+1:])


#Time Complexity - O(n)
#Space Complexity - O(1)        