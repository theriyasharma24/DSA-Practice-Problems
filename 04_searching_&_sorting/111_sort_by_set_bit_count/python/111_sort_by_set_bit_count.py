class Solution:
    def sortBySetBitCount(self, arr, n):
        arr.sort(key=lambda x: -bin(x).count('1'))
            
#Time Complexity: O(nlogn)
#Space Complexity: O(1)