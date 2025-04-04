#{ 
 # Driver Code Starts

# } Driver Code Ends

def reverse(S):
    stack=list(S)
    return "".join(stack[::-1])
    
    #Add code here


#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
        print("~")
# } Driver Code Ends

#Time Complexity: O(n)
#Space Complexity: O(n)