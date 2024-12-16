class Solution:
    def segregateElements(self, arr):
        l1,l2=[],[]
        for i in range(len(arr)):
            if arr[i]<0:
                l1.append(arr[i])
            else:
                l2.append(arr[i])
        arr[:]=l2+l1

#{ 
 # Driver Code Starts
def main():
    T = int(input())
    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a)
        print(*a)
        T -= 1
        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(n)