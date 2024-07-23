'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
'''

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0
        left=0
        right=len(nums)-1
        while(left<right):
            if(nums[left]+nums[right]<target):
                count += right -left
                left+=1
            else:
                right -=1
        return count
        