class Solution(object):
    
    def __init__(self):
        self.cdict = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cdict = {1:1, 2:2, 3:3}
        
        def get_permutations(n):
            if n <= 3:
                if n == 1:
                    return 1;
                elif n == 2:
                    return 2;
                elif n == 3:
                    return 3;
            else:
                if (n-2) in cdict.keys():
                    c_2 = cdict[n-2];
                else:
                    c_2 = get_permutations(n-2);

                if (n-1) in cdict.keys():
                    c_1 = cdict[n-1];
                else:
                    c_1 = get_permutations(n-1);
                return c_1 + c_2
        
        if n <= 3:
            return cdict[n]
        else:
            for i in range(3,n+1):
                cdict[i] = get_permutations(i)                
                
        return cdict[n];

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
    print(s.climbStairs(10))
