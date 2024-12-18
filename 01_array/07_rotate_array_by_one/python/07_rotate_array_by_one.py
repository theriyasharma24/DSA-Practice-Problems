class Solution:
    def rotate(self, arr):
        last_element = arr.pop()
        arr.insert(0, last_element)
        return arr

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(1)