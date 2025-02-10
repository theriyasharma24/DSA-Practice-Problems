class Solution:
    def find(self, arr, x):
        res=[]
        for i in range(len(arr)):
            if arr[i]==x:
                res.append(i)
                break
        if len(res)==0:
            return [-1,-1]
        else:
            for i in range(len(arr)-1,-1,-1):
                if arr[i]==x:
                    res.append(i)
                    break
            return res          

#{ 
 # Driver Code Starts
t = int(input())  # Number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array for each test case
    x = int(input())  # Element to search for
    ob = Solution()
    ans = ob.find(arr, x)  # Call the find function in the Solution class
    print(*ans)  # Print the result as space-separated values
    print("~")

# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)