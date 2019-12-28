import ipdb

dbg = ipdb.set_trace

       
class Solution(object):
    def longestPalindrome(self,arr):
        n = len(arr)

        max_len_arr = [[None for i in range(n)] for j in range(n)]
        ind_if_arr  = [[(None,None) for i in range(n)] for j in range(n)]

        max_len = 1
        indi = indf = 0
        for i in range(n):
            max_len_arr[i][i] = 1
            ind_if_arr[i][i]  = (i,i)

            if i != n-1:
                j = i+1
                pal_len = -1 if arr[i] != arr[j] else 2
                if pal_len > max_len:
                    max_len = pal_len; indi = i; indf = i+1;
                max_len_arr[i][j] = pal_len

        #dbg()
        for gap in range(2,n):
            for i in range(n):
                j = i+gap
                if j > n-1:
                    break
                else:
                    if max_len_arr[i+1][j-1] != -1:
                        pal_len = -1 if arr[i] != arr[j] else j-i+1
                        if pal_len > max_len:
                            max_len = pal_len; indi = i; indf = j;
                        max_len_arr[i][j] = pal_len
                    else:
                        max_len_arr[i][j] = -1
        #dbg()
        return arr[indi:indf+1]

if __name__ == "__main__":
    s = Solution()
    print(s.maxPalindrome("kayakaa"))
