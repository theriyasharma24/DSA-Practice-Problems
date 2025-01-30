class Solution:
    def areIsomorphic(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        d1={}
        d2={}
        for i in range(len(s1)):
            d1[s1[i]]=d1.get(s1[i],0)+1
            d2[s2[i]]=d2.get(s2[i],0)+1

        return list(d1.values())==list(d2.values())

#{ 
 # Driver Code Starts
import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        ob = Solution()
        if (ob.areIsomorphic(s, p)):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends

#Time Complexity - O(n)
#Space Complexity - O(n)