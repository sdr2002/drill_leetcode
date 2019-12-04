class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        max_sum = nums[0]
        amax_i = 0
        amax_f = 0

        new_i = 0
        new_f = 0
        growing_max = [0 for i in range(n)]; growing_max[0] = nums[0];
        for i in range(1,n):
            x = nums[i-1]

            if x > 0:
                growing_max[i] += x+nums[i]
                new_f = i
            else:
                growing_max[i] = nums[i]
                new_i = i
                new_f = i
            
            if max_sum < growing_max[i]:
                amax_i = new_i+0
                amax_f = new_f+0
                max_sum = growing_max[i]
            else:
                pass
            
        print('%s :: amax_i = %d / amax_f = %d / max_sum = %d'%(nums, amax_i, amax_f, max_sum))
        return max_sum

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4] ))
    print(s.maxSubArray( [-1,-2,-3] ))
