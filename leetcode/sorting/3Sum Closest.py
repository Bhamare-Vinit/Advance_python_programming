'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        dif=float('inf')
        for i in range(len(nums)):
            start = i+1
            end= len(nums)-1
            while start<end:
                sum=nums[i]+nums[start]+nums[end]
                if sum==target:
                    return target
                elif abs(target-sum)<dif:
                    dif=abs(target-sum)
                    ans=sum
                if sum>target:
                    end-=1
                else:
                    start+=1
        return ans

        