import ipdb
dbg = ipdb.set_trace

import string
puncs = list(string.punctuation)
import re
class Solution(object):    
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        wcount = dict()
        for w in re.split('\W+', paragraph):
            wlow = w.lower()
            wclean = ('').join([c for c in wlow if c not in puncs])
            if wclean in wcount.keys():
                wcount[wclean] += 1
            else:
                wcount[wclean] = 1

        for wban in banned:
            if wban in wcount:
                wcount.pop(wban)

        max_word = None
        max_count = None
        for w in wcount:
            if max_word is None:
                max_word = w
                max_count = wcount[w]
            else:
                if max_count < wcount[w]:
                    max_word = w
                    max_count = wcount[w]
                else:
                    pass

        return max_word


if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
    print(s.mostCommonWord("Bob!",["hit"]))
