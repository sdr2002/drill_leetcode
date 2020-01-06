import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)[::-1]

        memo = dict()
        def solve(cnArr,rem):
            if rem == 0:
                return 0
            elif rem < 0:
                return -1
            else:
                if rem in memo:
                    return memo[rem]
                else:
                    res_cnt_arr = list()
                    for cn in cnArr:
                        res_cnt = solve(cnArr,rem-cn)
                        if res_cnt != -1:
                            res_cnt_arr.append(res_cnt+1)
                        else:
                            continue
                    if len(res_cnt_arr) >0:
                        memo[rem] = min(res_cnt_arr)
                    else:
                        memo[rem] = -1
                    return memo[rem]               

        return solve(coins,amount)

if __name__ == "__main__":
    sol = Solution()
    prt = lambda **kwargs: print(sol.coinChange(**kwargs))

    #dbg()
    prt(coins = [1, 2, 5], amount = 100) #20
    prt(coins = [1, 2, 5], amount = 11)  #3
    prt(coins = [2, 5], amount = 3) #-1

    prt(coins = [186,419,83,408], amount = 6249) # 20

