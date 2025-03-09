class Solution:
    def romanToDecimal(self, s): 
        rom={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res,i=0,0
        while i<len(S):
            if i+1<len(S) and rom[S[i]]<rom[S[i+1]]:
                res+=rom[S[i+1]]-rom[S[i]]
                i+=2
            else:
                 res+=rom[S[i]]
                 i+=1
        return res

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
        print("~")

# } Driver Code Ends

#Time Complexity: O(n)
#Space Complexity: O(1)