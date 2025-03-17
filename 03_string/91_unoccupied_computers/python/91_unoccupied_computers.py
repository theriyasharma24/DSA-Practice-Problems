class Solution:
    def solve(self, n, s):
        occupied,in_cafe,ans = 0,{},0
        for customer in s:
            if customer in in_cafe:
                if in_cafe[customer]:
                    occupied -= 1
                del in_cafe[customer]
            else:
                if occupied < n:
                    occupied += 1
                    in_cafe[customer] = True
                else:
                    ans += 1
                    in_cafe[customer] = False
    
        return ans

#{ 
 # Driver Code Starts
for _ in range (int(input())):
    n = int(input())
    s = input().strip()
    ob = Solution()
    ans = ob.solve(n,s)
    print(ans)
    print("~")
# } Driver Code Ends

# Time Complexity: O(|S|)
# Space Complexity: O(1)