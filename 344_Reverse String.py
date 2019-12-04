class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n_list = len(s);
        is_n_odd = (n_list%2)==1;
        
        for i in range(n_list//2):
            ch_right = s[n_list-1-i]
            ch_left = s[i]
            s[i] = ch_right
            s[n_list-1-i] = ch_left
        
        return s


if __name__=='__main__':
    objt = Solution()
    print(objt.reverseString(["h","e","l","l","o"]))

    print(objt.reverseString(["h","e","l","l","o"]))

