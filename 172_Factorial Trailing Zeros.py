import ipdb

db = ipdb.set_trace

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: 
            return 0
        else:
            twos = 0
            fivs = 0

            zeros = 0

            #db()
            i = 1
            while (i<=n):
                twos += self.get_divs(2,i)
                fivs += self.get_divs(5,i)
                
                tens = min(twos,fivs)                
                zeros += tens
                twos -= tens
                fivs -= tens
                i += 1
            return zeros
        
    def get_divs(self,div,x):
        if x%div == 0:
            return 1+self.get_divs(div,x//div)
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(10))
