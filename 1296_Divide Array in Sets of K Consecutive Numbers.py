import ipdb
dbg = ipdb.set_trace

def update_consecs(arrs,k):
    # delete arrs with length >=k
    narrs = len(arrs)
    cnt = 0
    ind = 0
    while cnt < narrs:
        if len(arrs[ind]) == k:
            arrs.pop(ind)
        else:
            ind += 1
        cnt += 1

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nlen = len(nums)
        if (nlen == 0) or (nlen%k != 0) :
            return False
        
        nums = sorted(nums)

            
        inits = []
        while nums:        
            cur = nums[0]; dup = 1;
            nums.pop(0)
            while nums and (nums[0] == cur):
                dup += 1
                nums.pop(0)

            if len(inits)==0:
                [inits.append([cur]) for i in range(dup)]
            else:
                if all([consec[-1] == cur-1 for consec in inits]):
                    [consec.append(cur) for consec in inits]
                    dup -= len(inits)
                    update_consecs(inits,k)
                    [inits.append([cur]) for i in range(dup)]
                else:
                    return False
                                
        return True if len(inits)==0 else False


if __name__ == "__main__":
    sol = Solution().isPossibleDivide
    dbg()
    print(sol(nums = [1,2,3,3,4,4,5,6], k = 4))
    print(sol(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
    print(sol(nums = [3,3,2,2,1,1], k = 3))
    print(sol(nums = [3,3,3,2,2,2,1,1,1], k = 3))
    print(sol(nums = [1,2,3,4], k = 3))
