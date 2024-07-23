
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=[]
        num=nums1+nums2
        num.sort()
        n=len(num)
        if n%2==0:
            z=n//2
            e=num[z]
            q=num[z-1]
            ans=(e+q)/2
            return ans
        else:
            z=n//2
            ans=num[z]
            return ans