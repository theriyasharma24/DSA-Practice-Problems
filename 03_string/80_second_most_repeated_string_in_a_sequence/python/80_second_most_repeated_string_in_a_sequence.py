class Solution:
    def secFrequent(self, arr, n):
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]=d[arr[i]]+1
        d = dict(sorted(d.items(), key=lambda x: x[1],reverse=True))
        return list(d.keys())[1]
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends

# Time Complexity: O(nlogn)
# Space Complexity: O(n)