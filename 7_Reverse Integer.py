import math

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    #pdb.set_trace()
    sign = 1 if x>0 else -1;
    
    if ((x<-1*2**31) or (x>2**31-1)):
        return 0;
    elif (x==0):
        return 0;
    else:
        const_upbound = int(math.floor(math.log10(2**31)))
        x *= sign;
        
        isBiggestDiv_found = False;
        zero_found = False;
        
        highest_exp = const_upbound+0;
        
        parsed_ints = [];
        i = const_upbound+0;
        
        first_nonzero_dectected = False;
        while (i >= 0):
            
            coeff = x // (10**i);
            if ((coeff == 0) and not(first_nonzero_dectected)):
                i -= 1;
                continue;
            else:
                first_nonzero_dectected = True;
                parsed_ints.append(coeff);
                x = x % (10**i);
                i -= 1;
        
    #pdb.set_trace()
    #print('parsed_ints bef rev: %s'%parsed_ints)
    reved = 0;
    parsed_ints.reverse();
    n = len(parsed_ints);
    #parsed_ints.reverse();
    for i in range(n):
        c = parsed_ints[i];            
        reved += int(c *(10**(n-i-1)))

    return int(sign*reved);


if __name__=='__main__':
    print(reverse(123));
    print(reverse(-123));
    print(reverse(120));
    print(reverse(2**31));
    print(reverse(2**31-1));
    x = reverse(901000); assert x == 109, "Wrong 6: %d should be 109"%x;
    print(reverse(9646324351));
