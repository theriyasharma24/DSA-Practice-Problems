class Solution:    
    def findUnion(self, a, b):
        return len(set(a+b))

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findUnion(a, b))
        print("~")
# } Driver Code Ends

#Time Complexity - O(m+n)
#Space Complexity - O(m+n)