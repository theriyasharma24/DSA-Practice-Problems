class Solution:
    def rearrange(self,arr):
        positive=[i for i in arr if i>=0]
        negative=[i for i in arr if i<0]
        p,n=0,0
        for i in range(len(arr)):
            if (i%2==0 and p<len(positive) or n==len(negative)):
                arr[i]=positive[p]
                p+=1
            elif (i%2!=0 and n<len(negative) or p==len(positive)):
                arr[i]=negative[n]
                n+=1


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(n) 