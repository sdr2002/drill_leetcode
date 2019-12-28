import ipdb
dbg = ipdb.set_trace


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        else:
            ind_i = None
            ind_f = None
            
            dup = 1
            last_biggest_val  = nums[0]
            last_biggest_ind  = 0

            last_reversion = nums[0]
            for i in range(1,len(nums)):
                if last_biggest_val < nums[i]:
                    last_biggest_val = int(nums[i])
                    last_biggest_ind = int(i)
                elif last_biggest_val == nums[i]:
                    continue
                else:
                    ind_f = int(i)
                    for j in range(0,last_biggest_ind+1):
                        if nums[i] < nums[j]:
                            ind_i_cand = int(j) if j > 0 else 0
                            ind_i = ind_i_cand if (ind_i is None) or (ind_i_cand < ind_i) else ind_i
                            break
            dbg()
            if ind_i is None:
                return 0
            else:
                return ind_f - ind_i + 1


if __name__ == "__main__":
    s = Solution()
    dbg()
    print("2 ?= %d"%s.findUnsortedSubarray([3,2]))
    dbg()
    print("5 ?= %d"%s.findUnsortedSubarray([2,6,4,8,10,9,15]))
    dbg()
    print("3 ?= %d"%s.findUnsortedSubarray([2,3,3,2,4]))
    dbg()
    print("4 ?= %d"%s.findUnsortedSubarray([1,3,2,2,2]))
    dbg()
    print(s.findUnsortedSubarray([2,3,3,2,4]))
    dbg()
    print(s.findUnsortedSubarray([1,2,4,5,3]))
    dbg()
    print(s.findUnsortedSubarray([1,3,2,3,3]))
