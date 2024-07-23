'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        f=bisect_left(nums,target)
        l=bisect_right(nums,target)

        return [-1,-1] if f==l else [f,l-1]