class Solution:
    def reverseArray(self, arr):
        return arr.reverse()

#{ 
# Driver Code Starts
import sys
def main():
    tc = int(sys.stdin.readline())
    while tc > 0:
        str_arr = sys.stdin.readline().split()
        arr = [int(x) for x in str_arr]
        obj = Solution()
        obj.reverseArray(arr)
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")
        tc -= 1

if __name__ == "__main__":
    main()

# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)