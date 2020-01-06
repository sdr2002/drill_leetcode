class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d_c = dict({'2':['a','b','c']\
                    ,'3':['d','e','f']\
                    ,'4':['g','h','i']\
                    ,'5':['j','k','l']\
                    ,'6':['m','n','o']\
                    ,'7':['p','q','r','s']\
                    ,'8':['t','u','v']\
                    ,'9':['w','x','y','z']\
                   })
        
        ndig = len(digits)
        if ndig == 0:
            return []
        elif ndig == 1:
            return d_c[digits]
        else:        
            ret = list(d_c[digits[0]])
            for dig in digits[1:]:
                n_chars = len(d_c[dig])
                new_ret = list()
                for new_char in d_c[dig]:
                    new_ret.extend([st+new_char for st in ret])
                ret = new_ret
            return ret

if __name__ == "__main__":
    s = Solution()
    sol = s.letterCombinations      

    res = sol("")
    assert len(res)== 0
    print(res)

    res = sol("23")
    assert len(res)== 3*3
    print(res)

    res = sol("234689")
    assert len(res)== 3*3*3*3*3*4
    print(res)

    

