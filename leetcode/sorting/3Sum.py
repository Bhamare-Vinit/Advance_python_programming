'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()

        #splits number as positive ,negetive and zero
        p=[]
        n=[]
        z=[]
        for num in nums:
            if num>0:
                p.append(num)
            elif num<0:
                n.append(num)
            else:
                z.append(num)

        N,P=set(n),set(p)
        #for pairs such as (-2,0,2)
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num,0,num))
        #for pair of all zeros
        if len(z)>=3:
                res.add((0,0,0))
        
        #pairdc
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target=-1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))


        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target=-1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
            
        return res

        
                    

        