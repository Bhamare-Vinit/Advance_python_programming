'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        a=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    a+=1
        return a
        