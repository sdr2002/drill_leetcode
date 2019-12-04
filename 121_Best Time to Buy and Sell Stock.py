def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n_list = len(prices)
    #print('Series: %s'%prices)
    
    max_list = []
    highest_price = []

    highest_so_far = None
    for i in range(n_list-1,-1,-1):
        max_cand = prices[i]
        if i == n_list-1:
            highest_so_far = max_cand
        else:
            if highest_so_far < max_cand:
                highest_so_far = max_cand
            else:
                pass

        if highest_so_far is None:
            highest_price.append(None)
        else:
            highest_price.append(highest_so_far+0)

    highest_price.reverse()
    highest_price = highest_price[1:]

    maxmax=None
    for j in range(n_list-1):
        refprice = prices[j]
        highest  = highest_price[j]

        max_cand = highest-refprice
        if j == 0:
            maxmax = max_cand
        else:
            if maxmax < max_cand:
                maxmax = max_cand
            else:
                pass

    
    if maxmax is None:
        maxmax = 0

    print('maxmax=%d'%maxmax)
    return max(maxmax,0)

def maxProfit_naive(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n_list = len(prices)
    #print('Series: %s'%prices)
    
    max_list = []
    for i in range(n_list):
        max_for_i = 0
        amax_for_i = -1

        refprice = prices[i]
        #print('---i=%d----'%i)
        for j in range(i+1,n_list):
            new_price = prices[j]
            new_profit = new_price - refprice
            if j == i+1: # first j for i
                max_for_i = new_profit
            else:
                if max_for_i < new_profit:
                    max_for_i = new_profit
                else:
                    pass
            #print('<< max_for_i=%d at j=%d'%(new_profit,j))
                
        max_list.append(int(max_for_i+0))
    
    #print('max_list=%s'%max_list)

    maxmax = 0
    assert n_list==len(max_list)
    for k in range(n_list):
        new_maxmax_cand = max_list[k]
        if k == 0:
            maxmax = new_maxmax_cand
        elif maxmax < new_maxmax_cand:
            maxmax = new_maxmax_cand
        else:
            continue
            
    #print('maxmax=%d'%maxmax)
    return maxmax

if __name__=='__main__':
    maxProfit([3,2,6,5,0,3])
