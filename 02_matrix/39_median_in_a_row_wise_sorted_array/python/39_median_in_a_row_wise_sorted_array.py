class Solution:
    def median(self, mat):
        arr=[]
        for i in mat:
            arr+=i
        return sorted(arr)[(len(arr)//2)]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t = [int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j] = t[j]
        ans = ob.median(matrix)
        print(ans)
        print("~")
# } Driver Code Ends

#Time Complexity - O(nlogn)
#Space Complexity - O(n)