import math
class Solution:
    def countSquares(self, n):
        c=0
        for i in range(1,n+1):
            if (i**2)<n:
                c+=1
            else:
                return c


#{ 
 # Driver Code Starts
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countSquares(N))
        print("~")
# } Driver Code Ends

#Time Complexity: O(n)
#Space Complexity: O(1)