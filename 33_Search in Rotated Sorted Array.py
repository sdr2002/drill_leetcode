import ipdb
dbg = ipdb.set_trace

def isIn(v,l,r):
    return (l<=v) and (v<=r)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        
        def findInd(tg,il,ir):
            im = (il+ir)//2
            #print(il, im,ir)
            #dbg()
            if ir - il >= 2:                
                if not(isIn(tg,nums[il],nums[im])) and not(isIn(tg,nums[im],nums[ir])):
                    # This does not happen in sorted array
                    ind_cand = findInd(tg,il,im)
                    if ind_cand == -1:
                        return findInd(tg,im,ir)
                    else:
                        return ind_cand
                elif not(isIn(tg,nums[il],nums[im])) and (isIn(tg,nums[im],nums[ir])):
                    return findInd(tg,im,ir)
                elif (isIn(tg,nums[il],nums[im])) and not(isIn(tg,nums[im],nums[ir])):
                    return findInd(tg,il,im)
                else: 
                    # nums[im] == target
                    return im
                
            else:
                if ir-il == 0:
                    return -1 if nums[il] != tg else il
                elif ir-il == 1:
                    if nums[ir] == tg:
                        return ir
                    elif nums[il] == tg:
                        return il
                    else:
                        return -1

        return findInd(target,0,len(nums)-1)


if __name__ == "__main__":
    s = Solution()
    print(s.search([1,2,5,7,10,12,14,17,19],12),end='\n\n')    
    print(s.search([4,5,6,7,0,1,2],0),end='\n\n')
    print(s.search([4,5,6,7,0,1,2],3),end='\n\n')
