class Solution:
    def findMedian(self, arr):
        low=0
        upper=len(arr)
        sArr=sorted(arr)
        if upper%2!=0:
            mid=(upper+low)//2
            return sArr[mid]
        else:
            mid=(upper+low)//2
            return (sArr[mid]+sArr[mid-1])/2

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip()) 
    for _ in range(t):
        arr = list(map(int,
                       input().strip().split())
                   ) 
        solution = Solution()
        ans = solution.findMedian(
            arr)  
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
if __name__ == "__main__":
    main()
# } Driver Code Ends

#Time Complexity - O(nlogn)
#Space Complexity - O(n)
