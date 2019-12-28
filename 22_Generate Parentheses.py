import ipdb
dbg = ipdb.set_trace

"""
See http://www.iro.umontreal.ca/~pift2125/Current/Notes/catalan.pdf for catalan number counting the possible combinations of parentheses set
"""
class Solution(object):
    def generateParenthesis(self, num):
        """
        :type n: int
        :rtype: List[str]
        """
        arrs = []

        if num == 1:
            return ["()"]
        else:        
            def f(last_pos_list,ind):
                for pos in range(last_pos_list[-1],num):
                    if pos < ind:
                        continue
                    else:
                        if ind != num-1:
                            f(last_pos_list+[pos],ind+1)
                        else:
                            arrs.append(last_pos_list+[pos])
                return
            
            for i in range(num):
                f([i],1)

            return [ self.inds_to_str(num,arr) for arr in arrs ]
                            
    def inds_to_str(self,n,rinds):
        ss = ''                
        for i in range(n):
            ss += '('
            while (len(rinds)>0) and (rinds[0] <= i):
                ss += ')'
                rinds.pop(0)            
        return ss

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(4))
