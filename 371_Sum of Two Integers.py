import ipdb
db = ipdb.set_trace


class Solution(object):
    def getSum(self, x, y):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_int = 2**8-1
        min_int = -(2**8)
        mask = 2**8
        
        db()
        while not(y==0):
            temp_xor = (x^y)

            temp_and = (x&y)
            y = temp_and << 1
            x = temp_xor
            
        return x

if __name__ == "__main__":
    s = Solution()
    print(s.getSum(1,2))

    """
    x  = 1,1111111
    y  = 0,0000001

    ^  = 1,1111110
    &<<= 0,0000010

    ...

    ^  = 1,0000000
    &<<= 1,0000000

    ^  = 0,0000000
    &<<= 0,0000000
    """
    print(s.getSum(-1,1))
