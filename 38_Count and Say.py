import ipdb
idbg = ipdb.set_trace
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = int(n)
        if num == 1:
            return "1"
        else:
            ind = 1
            seq  = "1"
            
            while (ind < num):
                seq = self.convert(seq)
                ind += 1
            return seq

    def convert(self, seq):
        ### New gen
        #idbg()

        n_seq = len(seq)
        if n_seq == 0:
            return ""
        elif n_seq == 1:
            return "1%s"%seq
        else:
            primer = seq[0]
            n_dup  = self.compress(primer, seq[1:])
            
            substr = "%s%s"%(n_dup+1,primer)
            return substr + self.convert(seq[n_dup+1:])

    def compress(self, primer, subs):
        if primer == subs[0]:
            if len(subs) == 1:
                return 1
            else:
                return 1+self.compress(primer, subs[1:])
        else:
            return 0

def test_conversion(cstr, s=Solution()):
    print("%s -> %s"%(cstr,s.convert(cstr)))
    return

if __name__ == "__main__":
    s = Solution()
    test_conversion("1")
    test_conversion("11")
    test_conversion("21")
    test_conversion("1211")
    test_conversion("111221")

    print(s.countAndSay(15))
#    n=3; print("%d: %s"%(n,s.countAndSay()))
