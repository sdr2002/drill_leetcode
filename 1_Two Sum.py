import collections, bisect

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n_nums = len(nums)
        odict = collections.OrderedDict()
        for i in range(n_nums):
            odict[nums[i]] = []
        for i in range(n_nums):
            odict[nums[i]].append(i)
        odict = collections.OrderedDict(sorted([(k,v) for k,v in odict.items()]))

        print('odict:\n %s'%odict.items())

        nums_sorted = [k for k in odict.keys()]
        print('nums_sorted= %s'%nums_sorted)  
        
        n_vals = len(nums_sorted)
        for j in range(n_vals):
            v0 = nums_sorted[j]
            if (len(odict[v0])>1) and (v0*2==target):
                ind0, ind1 = odict[v0]
                break;
            else:
                ind0 = odict[v0][0];
                margin = target-nums_sorted[j]
                if margin in odict:
                    ind1 = odict[margin][0]
                    break
                else:
                    continue
        
        if ind0 > ind1:
            return [ind1,ind0]
        else:
            return [ind0,ind1]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1,6,3,4,9],12), end='\n\n')# [2,4]
    print(s.twoSum([3,3],6), end='\n\n') # [2,4]
    print(s.twoSum([0,4,3,0],0), end='\n\n') # [0,3]
    print(s.twoSum([-1,-2,-3,-4,-5],-8), end='\n\n') # [2,4]
    print(s.twoSum([3,2,3],6), end='\n\n') # [0,2]
    print(s.twoSum([-3,4,3,90],0), end='\n\n') # [0,2]
