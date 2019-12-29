import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm
        """
        nlen = len(height)
        
        l_cand = l_max = 0
        r_cand = r_max = nlen-1  
        
        area = lambda l, r: (r-l)*min(height[l],height[r])
        max_area = area(l_cand,r_cand)
        
        while l_cand < r_cand:
            ar = area(l_cand,r_cand)
            if max_area < ar:
                max_area = ar
                #l_max = l_cand
                #r_max = r_cand
                
            if height[l_cand] < height[r_cand]:
                l_cand += 1
            else:
                r_cand -= 1
                
        #print(l_max,r_max,max_area)
        return max_area

if __name__ == "__main__":
    s = Solution()
    sol = s.maxArea
    prt = lambda arg: print(sol(arg))

    prt([1,8,6,2,5,4,8,3,7]) # 49
    prt([2,3,4,5,18,17,6]) # 17
