class Solution:
    def minFlips(self, S):
        c1,c2=0,0
        for i in range(len(S)):
            if i%2==0 and S[i]!="0":
                c1+=1
            elif i%2==0 and S[i]!="1":
                c2+=1
            elif i%2!=0 and S[i]!="1":
                c1+=1
            else:
                c2+=1
        return(min(c1,c2))
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends

# Time Complexity: O(N)
# Space Complexity: O(1)