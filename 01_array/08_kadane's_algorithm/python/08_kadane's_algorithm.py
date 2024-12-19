class Solution:
    def maxSubArraySum(self,arr):
        max_so_far, max_ends_here=float('-inf'), 0        
        for i in range(len(arr)):
            max_ends_here=max(arr[i],max_ends_here+arr[i])
            max_so_far=max(max_so_far,max_ends_here )
        return max_so_far


#{ 
 # Driver Code Starts
import math
def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxSubArraySum(arr))
        T -= 1
if __name__ == "__main__":
    main()
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)