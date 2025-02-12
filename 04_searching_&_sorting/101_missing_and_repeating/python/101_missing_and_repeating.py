class Solution:
    def findTwoElement( self,arr): 
        r,d=[],{}
        for num in arr:
            if num in d:
                r.append(num)
            else:
                d[num]=1
        for i in range(1,len(arr)+1):
            if i not in d:
                r.append(i)
                break
        return r

#{ 
 # Driver Code Starts
if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends

#Time Complexity: O(n)
#Space Complexity: O(n)