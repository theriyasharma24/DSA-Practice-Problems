class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i, j, k = 0, 0, 0
        result = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        return result if result else [-1]
                
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))
        print("~")
# } Driver Code Ends


#Time Complexity - O(n1+n2+n3)
#Space Complexity - O(1)