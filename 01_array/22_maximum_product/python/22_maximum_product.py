class Solution:
    def maxProduct(self, arr):
        currMax, currMin, res = 1, 1, max(arr)
        for i in range(len(arr)):
            if arr[i] < 0:
                currMax, currMin = currMin, currMax
            currMax = max(arr[i] * currMax, arr[i])
            currMin = min(arr[i] * currMin, arr[i])
            res = max(res, currMax)
        return res


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Input array
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)
