class Solution:
    def isPowerofTwo(self, n):
         return n > 0 and (n & (n - 1)) == 0





#{ 
 # Driver Code Starts
import math


def main():

    T = int(input())

    while (T > 0):

        n = int(input())
        ob = Solution()
        if ob.isPowerofTwo(n):
            print("true")
        else:
            print("false")

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends

# Time Complexity: O(1)
# Space Complexity: O(1)