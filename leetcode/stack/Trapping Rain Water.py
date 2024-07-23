'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        LMAX,RMAX=height[l],height[r]
        result=0
        while l<r:
            if LMAX<RMAX:
                l+=1
                LMAX=max(LMAX,height[l])
                result+=LMAX-height[l]
            else:
                r-=1
                RMAX=max(RMAX,height[r])
                result+=RMAX-height[r]
        return result