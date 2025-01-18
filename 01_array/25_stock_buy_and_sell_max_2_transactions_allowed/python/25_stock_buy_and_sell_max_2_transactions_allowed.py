from typing import List
class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        buy,sell,buy1,sell1 = float('inf'),0,float('inf'),0
        for p in price:
            buy = min(buy, p)
            sell = max(sell, p - buy)
            buy1 = min(buy1, p - sell)
            sell1 = max(sell1, p - buy1)
        return sell1

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        price=IntArray().Input(n)
        obj = Solution()
        res = obj.maxProfit(n, price)
        print(res)
        print("~")
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)