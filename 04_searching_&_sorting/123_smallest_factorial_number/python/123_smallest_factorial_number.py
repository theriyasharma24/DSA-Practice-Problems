class Solution:
    def findNum(self, n: int):
        res, num, c = 0, 5, 0  
        def count_trailing_zeros(n):
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count
        while res == 0:
            c = count_trailing_zeros(num)  
            if c >= n:  
                res = num
                return res  
            num += 5         

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
        print("~")
# } Driver Code Ends

#Time Complexity: O(nlog(n))
#Space Complexity: O(1)