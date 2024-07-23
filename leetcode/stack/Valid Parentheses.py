'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # while len(s) > 0:
        #     l = len(s)
        #     s = s.replace('()','').replace('{}','').replace('[]','')
        #     if l==len(s): return False
        # return True
        li=[]
        for i in s:
            if i in ['(','{','[']:
                li.append(i)
            elif i ==")":
                if len(li)==0:
                    return False
                if li[-1] == "(":
                    li.pop()
                else:
                    return False
            elif i =="}":
                if len(li)==0:
                    return False
                if li[-1] == "{":
                    li.pop()
                else:
                    return False
            elif i =="]":
                if len(li)==0:
                    return False
                if li[-1] == "[":
                    li.pop()
                else:
                    return False
        if len(li)==0:
            return True 
        else:
            return False
            
        