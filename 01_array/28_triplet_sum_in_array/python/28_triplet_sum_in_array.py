class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n=len(arr)
        for i in range(n-1):
            left = i+1
            right = n-1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == target:
                    return 1
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
        return 0

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array
        target = int(input().strip())  # Read the target sum
        ob = Solution()
        print("true"
              if ob.hasTripletSum(arr, target) else "false")  # Output result
        tc -= 1

# } Driver Code Ends

#Time Complexity - O(n^2)
#Space Complexity - O(n)