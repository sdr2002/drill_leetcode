import ipdb

dbg = ipdb.set_trace

class Solution(object):
    def maxLoss(self,pnls):
        # subarr = argmin sum(subarr)
        
        n = len(pnls)

        ml_arr = [None for i in range(n)]
        indi_arr = [None for i in range(n)]
        indf_arr = list(range(n))

        # get ml_arr, indi_arr, indf_arr
        ml_arr[0] = pnls[0]; indi_arr[0] = 0; indf_arr[0] = 0;
        for i in range(1,n):
            x = pnls[i]
            if ml_arr[i-1] < 0:
                ml_arr[i] = x + ml_arr[i-1]
                indi_arr[i] = indi_arr[i-1]
            else:
                ml_arr[i] = x
                indi_arr[i]  = i

        # find min ml_arr and retrieve ind and indf
        min_pnl = min_indi = min_indf = None
        for i in range(n):
            min_ml_i = ml_arr[i]
            if min_pnl is None:
                min_pnl  = min_ml_i
                min_indi = indi_arr[i]
                min_indf = i
            elif min_pnl > min_ml_i:
                min_pnl  = min_ml_i
                min_indi = indi_arr[i]
                min_indf = i
            else:   
                pass

        return min_pnl, min_indi, min_indf


if __name__ == "__main__":
    s = Solution()
    print(s.maxLoss([5,-3,-1,2,6,-3,4])) # -4, 1, 2
    print(s.maxLoss([1,-1,2,-2,-3,7])) # -5, 3, 4
    print(s.maxLoss([1,-1,1,-2,-2])) # -4, 3, 4
