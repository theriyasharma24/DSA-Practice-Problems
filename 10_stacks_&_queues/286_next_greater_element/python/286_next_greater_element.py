class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n 
        stack = [] 

        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                ans[index] = arr[i]
            stack.append(i)

        return ans

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends

#Time Complexity: O(n)
#Space Complexity: O(n)