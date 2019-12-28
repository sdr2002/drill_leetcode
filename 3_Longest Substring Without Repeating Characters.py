class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        nstr = len(s)
        
        max_n = 1
        max_indi = 0
        max_indf = 0
        paststr = s[0] # str of unique chars
        
        ind_i  = 0
        ind_f  = 0
        for i in range(1,nstr):
            c = s[i]
            if c in paststr:
                ind_i   = paststr.index(c)+1
                paststr = paststr[ind_i:]+c                
            else:
                paststr += c                
            ind_f = int(i)
            
            if len(paststr) > max_n:
                max_n = len(paststr)
                max_indi  = int(ind_i)
                max_indf  = int(ind_f)
                
                
        return max_n
        
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
