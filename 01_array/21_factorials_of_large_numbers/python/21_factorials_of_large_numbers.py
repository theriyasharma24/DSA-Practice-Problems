class Solution:
    def factorial(self, n):
        fact=1
        l=[]
        for i in range(1,n+1):
            fact*=i
        for i in str(fact):
            l.append(int(i))
        return l

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        print(" ".join(
            str(i) for i in
            ans)) 
        print("~")
# } Driver Code Ends

#Time Complexity - O(nlogn)
#Space Complexity - O(nlogn)