class Solution:
    def mergeSort(self,arr, l, r):
        if l<r:
            mid=(l+r)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)
    def merge(self,arr,l,mid,r):
        n1 = mid - l + 1
        n2 = r - mid
        L = [0] * n1
        R = [0] * n2
        for i in range (n1):
            L[i]=arr[l+i]
        for i in range(n2):
            R[i]=arr[mid+1+i]
        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1
# } Driver Code Ends

#Time Complexity: O(nlogn)
#Space Complexity: O(1)