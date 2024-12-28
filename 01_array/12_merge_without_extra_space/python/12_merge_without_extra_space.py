class Solution:
    def mergeArrays(self, a, b):
        i = len(a) - 1
        j = 0
        while i >= 0 and j < len(b):
            if a[i] < b[j]:
                i -= 1
            else:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
        a.sort()
        b.sort()

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        solution = Solution()
        solution.mergeArrays(a, b)
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))
        print("~")
# } Driver Code Ends

#Time Complexity - O(nlogn + mlogm)
#Space Complexity - O(1)