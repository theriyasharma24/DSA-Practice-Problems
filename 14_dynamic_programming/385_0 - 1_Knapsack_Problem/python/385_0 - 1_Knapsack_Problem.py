class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(values[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[n][W]



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends

# Time Complexity: O(n * W)
# Space Complexity: O(n * W)