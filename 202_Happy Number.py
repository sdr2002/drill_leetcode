class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        pass
    
    def isNumHappy(self, num, oneExisted=False):
        if num == 0:
            return oneExisted
        elif num == 1:
            return True if not(oneExisted) else False
        elif num > 1:
            return False
        else:
            if num//10 == 1:
                if oneExisted:
                    return False
                else:
                    return self.isNumHappy(num//10,True)
            elif num//10 > 1:
                return False
            else:
                return self.isNumHappy(num//10, oneExisted)


if __name__ == '__main__':
    s = Solution()
    print(s.isNumHappy(1))
    print(s.isNumHappy(0))
    print(s.isNumHappy(10))
