class Solution:
    def removeDuplicates(self, s):
        s1=""
        for i in s:
            if i not in s1:
                s1+=i
        return s1

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends

#Time Complexity: O(N)
#Space Complexity: O(N)