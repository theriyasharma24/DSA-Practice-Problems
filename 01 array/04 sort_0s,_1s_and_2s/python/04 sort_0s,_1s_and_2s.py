class Solution:
    def sort012(self, arr):
        low,mid,high=0,0,len(arr)-1
        while mid<=high:
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip()) 
    ob = Solution()
    while t > 0:
        t -= 1
        arr = list(map(int,input().strip().split())) 
        ob.sort012(arr) 
        print(' '.join(map(str, arr)))  
        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends


#Algorithm Used - Dutch National Flag Algorithm (It is an efficient algorithm for sorting an array containing only three distinct elements. It is often used in problems involving sorting an array of 0s, 1s, and 2s in O(n) time and O(1) space).
#Time Complexity - O(n)
#Space Complexity - O(1)