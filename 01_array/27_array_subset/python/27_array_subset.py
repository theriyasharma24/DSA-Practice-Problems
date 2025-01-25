class Solution:
    def isSubset(self, a, b):
        return set(b).issubset(set(a))

#{ 
 # Driver Code Starts
def main():
    T = int(input())
    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")
        T -= 1
        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends

#Time Complexity - O(n1+n2)
#Space Complexity - O(n1+n2)