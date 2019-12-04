class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        return nums[-k:] + nums[:-k]


if __name__ == '__main__':
    s = Solution();
    print(s.rotate([1,2,3,4,5,6,7],3))
