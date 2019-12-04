def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    #print('\nS:\n%s'%S)
    agg = ('').join(S.split('-'))
    #print('>> agg:\n%s'%agg)

    n_chars = len(agg)
    if n_chars == 0:
        print('n_chars= 0, return ""')
        return ""
    elif K == 0:
        raise Exception('K=0, raise')
    else:
        n_chunks = n_chars//K
        if n_chars%K == 0:
            pass
        else:
            n_chunks += 1

        reformatted = ""
        subs = ""
        for i in range(n_chunks):
            if i == 0:
                n_chars_first = K if n_chars%K == 0 else n_chars-(n_chunks-1)*K
                subs = agg[:n_chars_first].upper()
            else:
                subs = "-" + agg[n_chars_first+(i-1)*K:n_chars_first+(i*K)].upper()
            #print('subs at i=%d:%s'%(i,subs))
            reformatted += subs

    #print('return:\n%s'%reformatted)

    return reformatted


if __name__=='__main__':
    licenseKeyFormatting(S = "5F3Z-2e-9-w", K = 4)
    licenseKeyFormatting(S = "2-5g-3-J", K = 2)
