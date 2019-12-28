import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        num = len(intervals)
        if num < 2:
            return num
        intvs = [intervals[i] for i in sorted(range(num), key = lambda k: intervals[k][0])]
        
        quos = [intvs[0]]
        for intv in intvs[1:]:
            noRoom = True
            ind = 0
            for quo in quos:
                if self.isOut(quo,intv[0]):
                    quos[ind] = [min(quo[0],intv[0]), max(quo[1],intv[1])]
                    noRoom = False
                    break
                ind += 1
            
            if noRoom:
                quos.append(intv)
                
        return len(quos)        
        
    def isOut(self,intv,v):
        return intv[1] <= v

if __name__ == "__main__":
    s = Solution()
    print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
    dbg()
    print(s.minMeetingRooms([[5, 8],[6, 8]]))
