class Solution:
    def medianOf2(self, a, b):
        l=sorted(a+b)
        n=len(l)
        mid=n//2
        if n%2!=0:
            return l[mid]
        else:
            return (l[mid]+l[mid-1])/2


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")

# } Driver Code Ends

#Time Complexity - O((n+m)log(n+m))
#Space Complexity - O(n+m)