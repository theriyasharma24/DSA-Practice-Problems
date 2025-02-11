class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0
        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1

#{ 
 # Driver Code Starts
import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)
#Algorithm - Moore's Voting Algorithm