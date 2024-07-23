'''
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
'''


class Solution:
    
    def maxDepth(self, s: str) -> int:
        li=[]
        maxi=0
        for i in s:
            if i =="(":
                li.append(i)
            if i==")":
                maxi=max(len(li),maxi)
                li.pop()
        return maxi
        