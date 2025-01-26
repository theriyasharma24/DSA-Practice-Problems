class Solution:
    def longestConsecutive(self,arr):
        arr.sort()
        res=1
        cnt=1
        for i in range(1,len(arr)):
            if(arr[i]==arr[i-1]):
                continue
            if(arr[i]==arr[i-1]+1):
                cnt+=1
            else:
                cnt=1
            res=max(res,cnt)
        return res


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
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends
#Time Complexity - O(nlogn)
#Space Complexity - O(1)