import ipdb

db = ipdb.set_trace

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = len(nums)
        
        db()
        if ns == 1:
            return nums[0]
        else:
            vn = dict()
            for v in nums[:ns//2+1]:
                if not(v in vn.keys()):
                    vn[v]  = 1
                else:
                    vn[v] += 1
            
            ind = ns//2+1
            while len(vn.keys()) > 1:
                v = nums[ind]
                if not(v in vn.keys()):
                    pass
                else:
                    vn[v] += 1
                    if vn[v] >= ns//2+1: return v
                    
                minors = []
                for k in vn.keys():
                    if vn[k] < ind - ns//2:
                        del vn[k]                
                ind += 1
                
            return vn.keys()[0]

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))
