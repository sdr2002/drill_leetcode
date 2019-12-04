class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        self.tar = x;
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.bi_srch(0, x, x//2)
        
                
    def bi_srch(self,xi,xf,test):
        # print('xi=%d / xf=%d / test=%d'%(xi,xf,test))
        # xi <= test <= xf
        if (xi**2 == self.tar):
            return xi
        elif (xf**2 == self.tar):
            return xf
        elif (test**2 == self.tar):
            return test
        elif (test**2 > self.tar):
            if ((test-1)**2 < self.tar):
                return test-1
            elif ((test-1)**2 == self.tar):
                return test-1
            else:
                return self.bi_srch(xi,test,xi+(test-xi)//2)
        elif (test**2 < self.tar):
            if ((test+1)**2 > self.tar):
                return test
            elif ((test+1)**2 == self.tar):
                return test+1
            else:
                return self.bi_srch(test,xf,test+(xf-test)//2)
        else:
            raise Exception("??")
        

if __name__ == '__main__':
    import sys
    s = Solution()
    print(s.mySqrt(int(sys.argv[1])))
