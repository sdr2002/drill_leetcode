import ipdb

dbg = ipdb.set_trace

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotn = set()
        frsh = set()
        r = 0
        for row in grid:
            c = 0
            for cell in row:
                if cell == 2:
                    rotn.add((r,c))
                elif cell == 1:
                    frsh.add((r,c))
                else:
                    pass
                c += 1
            r += 1        
        
        newrot=True
        iters = 0
                
        while newrot:
            newrotns = set()
            for ir, ic in rotn:
                for dRow, dCol in [(1,0),(-1,0),(0,1),(0,-1)]:
                    loc = (ir-dRow,ic-dCol)
                    if loc in frsh:
                        frsh.remove(loc)
                        newrotns.add(loc)
                    else:
                        pass
            
            if not(bool(newrotns)):
                newrot = False
            elif not(bool(frsh)):
                newrot = False
            else:
                rotn = set({l for l in newrotns})
            iters += 1
            
        if bool(frsh):
            return -1
        else:
            return iters                

if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
