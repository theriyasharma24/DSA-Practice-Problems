class Solution:
    def inSequence(self, a, b, c):
        if (b-a) % c == 0:
            return 1
        return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = int(input())
        B = int(input())
        C = int(input())
        ob = Solution()
        ans = ob.inSequence(A, B, C)
        if (ans):
            print("true")
        else:
            print("false")
# } Driver Code Ends

#Time Complexity: O(1)
#Space Complexity: O(1)