class Solution:
    def inversionCount(self, arr):
        def merge_sort_and_count(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
                inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
                inv_count += merge_and_count(arr, temp_arr, left, mid, right)
            
            return inv_count
        
        def merge_and_count(arr, temp_arr, left, mid, right):
            i, j, k = left, mid + 1, left
            inv_count = 0
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1) 
                    j += 1
                k += 1
            
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1
            
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1
            
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
            
            return inv_count

        n = len(arr)
        temp_arr = [0] * n
        return merge_sort_and_count(arr, temp_arr, 0, n - 1)





#{ 
 # Driver Code Starts
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")
# } Driver Code Ends

#Time Complexity - O(nlogn)
#Space Complexity - O(n+logn)