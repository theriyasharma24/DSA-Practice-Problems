class Solution:
    def rowWithMax1s(self, arr):
        count, row=0,-1
        for i in range(len(arr)):
            c=arr[i].count(1)
            if c>count:
                count=c
                row=i
        return row


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        input_line = input().strip()  # Read input matrix as string
        mat = eval(input_line)  # Convert string to matrix

        solution = Solution()
        result = solution.rowWithMax1s(mat)  # Get the row with the most 1s

        print(result)
        print("~")

# } Driver Code Ends

#Time Complexity - O(m*n)
#Space Complexity - O(1)