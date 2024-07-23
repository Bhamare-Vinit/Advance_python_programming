'''
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
'''

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
        sum=0
        for i in range(len(grid[0])):
            maxval=0
            for j in range(len(grid)):
                maxval=max(grid[j][i],maxval)
            sum+=maxval
        return sum