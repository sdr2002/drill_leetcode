import ipdb
dbg = ipdb.set_trace

import math
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def n_to_np1(arrN,new_int):
            l = len(arrN[0])
            arrNp1 = []
            for i in range(l+1):
                for arr in arrN:
                    arrNp1.append(arr[:i] + [new_int] + arr[i:] )
            return arrNp1

        num = len(nums)
        if num == 0:
            return [[]]
        elif num == 1:
            return [nums]
        else:
            arr = [[nums[0]]]
            i = 1
            while i < num:
                arr = n_to_np1(arr,nums[i])
                i += 1
            assert len(arr) == math.factorial(num), "len(arr) must be n!"
            return arr


if __name__ == "__main__":
    sol = Solution()
    prt = lambda *args: print(sol.permute(*args))

    #prt([])
    prt([1])
    #prt([1,2])
    #prt([1,2,3])
    #prt([1,2,3,4])
