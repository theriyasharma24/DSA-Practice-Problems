def isPalinArray(arr):
    for i in arr:
        s=str(i)
        if s != s[::-1]:
            return False
    else:
        return True

#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if isPalinArray(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends

#Time Complexity - O(n*k)
#Space Complexity - O(1)