import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        remainder = int(numerator)
        isNeg = 1 if remainder<0 else 0
        dec = 0

        div_rem = []
        #dbg()
        if abs(remainder) < denominator:
            div_rem.append((0,remainder))
        else:
            div = remainder // denominator + isNeg*int((remainder % denominator)!=0)
            remainder = (remainder % denominator) - isNeg*denominator*int((remainder % denominator)!=0)
            div_rem.append((div,remainder))

        #dbg()
        if remainder != 0:
            zeros = 0
            while remainder != 0:
                if abs(remainder) < denominator:
                    div = 0
                    remainder *= 10
                    div_rem.append((div,remainder))
                else:
                    div = remainder // denominator + isNeg*int((remainder % denominator)!=0)
                    remainder = (remainder%denominator) - isNeg*denominator*int((remainder % denominator)!=0)
                    div_rem.append((div,remainder))

                    if remainder == 0:
                        case = "end"
                        break
                    elif (div,remainder) in div_rem[1:-1]:
                        case = "rep"
                        break
                    else:
                        continue
        else:
            pass

        rev_div_rem_no_zeros = []
        #dbg()
        n_zeros = 0
        for ind in range(len(div_rem))[::-1]:
            if (div_rem[ind][0] != 0) or (n_zeros==0):
                rev_div_rem_no_zeros.append(div_rem[ind])
                if div_rem[ind][0] != 0:
                    n_zeros = len(str(abs(div_rem[ind][0])))
                else:
                    n_zeros = 0

            else:
                if n_zeros > 0:
                    n_zeros-=1
                    continue
                else:
                    rev_div_rem_no_zeros.append(div_rem[ind])

        div_rem = rev_div_rem_no_zeros[::-1]
        #dbg()
        signStr = '-' if isNeg==1 else ''
        if len(div_rem)==1:
            return signStr+str(abs(div_rem[0][0]))
        else:
            if case == "end":
                return signStr+ str(abs(div_rem[0][0])) +'.'+ ('').join([str(abs(v[0])) for v in div_rem[1:]])
            elif case == "rep":                
                ind_i_rep = div_rem[1:].index(div_rem[-1]) + 1
                sub = 1
                while (div_rem[ind_i_rep-sub] == div_rem[-1-sub]):
                    sub += 1
                ind_i_rep -= (sub-1)

                return signStr+ str(abs(div_rem[0][0])) +'.'\
                        +('').join([str(abs(v[0])) for v in div_rem[1:ind_i_rep]])\
                        +'('+('').join([str(abs(v[0])) for v in div_rem[ind_i_rep:-sub]])+')'
            else:
                raise Exception("Unexpected")


if __name__ == "__main__":
    sol = Solution()
    prt = lambda **kwargs: print(sol.fractionToDecimal(**kwargs))

    prt(numerator = 2, denominator = 1)

    prt(numerator = 1, denominator = 2)
    prt(numerator = 1, denominator = 8)

    prt(numerator = 9, denominator = 8)
    prt(numerator = 201, denominator = 8)
    prt(numerator = 2001, denominator = 8)

    prt(numerator = 8, denominator = 125)
    prt(numerator = 257, denominator = 125)


    prt(numerator = 1, denominator = 6)
    prt(numerator = 7, denominator = 6)
    
    #dbg()
    prt(numerator = 2, denominator = 33)
    prt(numerator = 35, denominator = 33)
    prt(numerator = 200, denominator = 14)
    prt(numerator = 20, denominator = 14)
    prt(numerator = 2, denominator = 14)

    prt(numerator = -50, denominator = 8)
    prt(numerator = 7, denominator = -12)
    prt(numerator = -7, denominator = -12)
