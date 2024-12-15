class Solution:
    def get_min_max(self, arr):
        minimumElement,maximumElement=float('inf'),0
        for i in arr:
            if i<minimumElement:
                minimumElement=i
            if i>maximumElement:
                maximumElement=i
        return minimumElement, maximumElement

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)