'''
Given an array of integers heights representing the histogram's bar height where 
the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    n = len(heights)
    left, right = [0] * n, [0] * n
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack = []
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)
    max_area = 0
    for i in range(n):
        max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))
    return max_area

        