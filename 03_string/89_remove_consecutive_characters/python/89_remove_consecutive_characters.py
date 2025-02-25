class Solution:
    def removeConsecutiveCharacter(self, s):
        lastElement,ans = '',[]
        for i in s:
            if i != lastElement:
                ans.append(i)
            lastElement = i
        return ''.join(ans) 

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

        print("~")
# } Driver Code Ends

#Time Complexity: O(N)
#Space Complexity: O(N)