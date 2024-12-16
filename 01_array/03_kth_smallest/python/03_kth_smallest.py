import heapq
class Solution:
    def kthSmallest(self, arr,k):
        heapq.heapify(arr) #min heap
        
        for i in range(k-1):
            heapq.heappop(arr)
        return heapq.heappop(arr)

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends

#Algorithm Used - Min-Heap
#Time Complexity - O(n+klogn)
#Space Complexity - O(n)