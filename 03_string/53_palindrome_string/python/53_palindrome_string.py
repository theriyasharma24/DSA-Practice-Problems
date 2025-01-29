class Solution:
    def isPalindrome(self, s: str) -> bool:
		if s==s[::-1]:
		    return True
		else:
		    return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(n)