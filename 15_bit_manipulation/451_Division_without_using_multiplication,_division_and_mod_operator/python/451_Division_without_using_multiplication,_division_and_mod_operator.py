class Solution:
    def divide(self, dividend, divisor):
        sign=1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        
        return (sign)*(dividend//divisor)

#Time Complexity: O(1)
#Space Complexity: O(1)