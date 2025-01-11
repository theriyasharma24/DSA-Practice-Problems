class Solution:
    def countOccurence(self,arr, k):
        times=len(arr)//k
        d={}
        count=0
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key,value in d.items():
            if value>times:
                count+=1
        return count
#{ 
 # Driver Code Starts
import bisect
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countOccurence(A, D)
        print(ans)
        print("~")
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(n)