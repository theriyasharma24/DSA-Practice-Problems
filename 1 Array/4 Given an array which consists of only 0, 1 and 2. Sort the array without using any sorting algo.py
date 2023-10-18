#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        left, curr, right = 0, 0, len(arr) - 1

        while curr <= right:
            if arr[curr] == 0:
                # Swap the element at the left pointer with the current element
                arr[left], arr[curr] = arr[curr], arr[left]
                left += 1
                curr += 1
            elif arr[curr] == 1:
                curr += 1
            else:  # nums[curr] == 2
                # Swap the element at the right pointer with the current element
                arr[curr], arr[right] = arr[right], arr[curr]
                right -= 1
        return arr
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
