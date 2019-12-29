import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        prevs = [s]
        wordDict = sorted(wordDict)
        #dbg()
        while True:        
            nexts = []
            for prev in prevs:
                for word in wordDict:
                    if  word[0] > prev[0]:
                        break
                    else:
                        if len(prev) >= len(word):
                            if prev[:len(word)] == word:
                                a_next = prev[len(word):]
                                if len(a_next) == 0:
                                    return True
                                else:
                                    nexts.append(a_next)
                        else:
                            continue
                            
            #dbg()
            nexts = sorted(list(set(nexts)))
            if (len(nexts)==0) or (nexts == sorted(prevs)):
                return False
            else:
                prevs = nexts


if __name__ == "__main__":
    s = Solution()

    print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
    print(s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
    print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
    
