class Solution:
    def middle(self, a, b, c):
        if (b>a or c>a) and (b<a or c<a):
            return a
        elif (a>b or c>b) and (a<b or c<b):
            return b
        else:
            return c

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = int(input())
        B = int(input())
        C = int(input())
        ob = Solution()
        print(ob.middle(A, B, C))
        print("~")
# } Driver Code Ends

#Time Complexity: O(1)
#Space Complexity: O(1)