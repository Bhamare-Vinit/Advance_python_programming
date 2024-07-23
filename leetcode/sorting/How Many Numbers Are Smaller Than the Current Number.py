'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ans = []
        
#         for i in range(len(nums)):
#             x=0
#             for j in range(len(nums)):
#                 if nums[i]> nums[j]:
#                     x+=1
#             ans.append(x) 
#         return ans       
                    
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            a.append(len([x for x in nums if x<i]))
        return a