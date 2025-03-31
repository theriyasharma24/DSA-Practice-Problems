class Solution:
    def minSwaps(self, nums):
        s = sorted(nums)
        if s == nums:
            return 0

        count, d = 0, {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
        for i in range(0, len(nums)):
            if nums[i] != s[i]:
                n = d[s[i]]
                nums[i], nums[n] = nums[n], nums[i]
                count += 1
                d[nums[n]] = n
                d[nums[i]] = i
        return count

# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minSwaps(arr)
        print(res)
        t -= 1
# Driver Code Ends

#Time Complexity: O(NlogN)
#Space Complexity: O(N)