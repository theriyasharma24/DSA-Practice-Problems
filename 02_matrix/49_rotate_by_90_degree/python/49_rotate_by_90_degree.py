def rotate(mat): 
    n = len(mat)
    m = len(mat[0])
    for i in range(n - 1):
        for j in range(i, m):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(n):
        mat[i].reverse()
    return mat

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")
# } Driver Code Ends

#Time Complexity: O(N^2)
#Space Complexity: O(1)