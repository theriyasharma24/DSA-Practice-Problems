class Solution:
	def setBits(self, n):
	    return bin(n).count("1")
	    
	
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)

        print("~")

# } Driver Code Ends

#Time Complexity: O(log n) 
#Space Complexity: O(log n) 