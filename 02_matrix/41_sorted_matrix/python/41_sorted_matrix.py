class Solution:
    def sortedMatrix(self,N,Mat):
        l=[]
        for i in Mat:
            l.extend(i)
        l.sort()
        Mat=[]
        for i in range(0,N*N,N):
            Mat.append(l[i:i+N])
        return Mat

#{ 
 # Driver Code Starts

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends

#Time Complexity - O(n^2logn)
#Space Complexity - O(n^2)