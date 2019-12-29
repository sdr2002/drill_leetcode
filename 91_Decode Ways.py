import ipdb
dbg = ipdb.set_trace

def case1(s):
    if s == '0':
        return 0
    else:
        return 1
    
def case2(s):
    if s[0] == '0':
        return 0
    elif s[0] in set({'1','2'}):
        if s[1] == '0':
            return 1
        elif int(s) <= 26:
            return 2
        else:
            return 1
    else:
        if s[1] == '0':
            return 0
        else:
            return 1       
        
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return case1(s)
        elif len(s) == 2:
            return case2(s)
        else:
            nums = [-1 for i in s]
            nums[0] = case1(s[0])
            if (nums[0] == 0): 
                return 0
            nums[1] = case2(s[:2])

            for i in range(2,len(s)):
                nums[i] = (nums[i-1]-nums[i-2]*case1(s[i-1]))*case1(s[i]) + nums[i-2]*case2(s[i-1:i+1])

            return nums[-1]
                
                
if __name__ == "__main__":
    sol = Solution().numDecodings

    assert 2==sol("12"); assert 2==sol("21"); assert 1==sol("27"); assert 2==sol("26"); assert 1==sol("20");
    assert 0==sol("01"); assert 0==sol("30"); assert 1==sol("39"); assert 0==sol("0");  assert 1==sol("1");

    dbg()
    assert 3 == sol("123"); assert 3 == sol("226"); assert 0 == sol("230"); assert 2 == sol("239");
    assert 0 == sol("012"); assert 2 == sol("17");

    assert 3 == sol("1239")

