class Solution:
    def valueEqualToIndex(self, arr):
        l=[]
        for i in range(len(arr)):
            if arr[i]==i+1:
                l.append(arr[i])
        return l

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1
        print("~")

# } Driver Code Ends

# Time Complexity: O(n)
# Space Complexity: O(n)