class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        j=1
        while j<len(intervals):
            if intervals[j-1][1]>=intervals[j][0]:
                a,b=0,0
                if intervals[j-1][0]<intervals[j][0]:
                    a=intervals[j-1][0]
                else:
                    a=intervals[j][0]
                if intervals[j-1][1]<intervals[j][1]:
                    b=intervals[j][1]
                else:
                    b=intervals[j-1][1]
                pair=[a,b]
                intervals.pop(j-1)
                intervals[j-1]=pair
            else:
                j+=1
        return intervals


#Time Complexity - O(nlogn)
#Space Complexity - O(n)

        