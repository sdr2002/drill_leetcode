import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #dbg()

        if beginWord == endWord: 
            return 0
        else:
            while beginWord in wordList:
                wordList.pop(wordList.index(beginWord))

            nchars = len(beginWord)
            key_dict = dict()
            #dbg()
            for word in wordList:
                for i in range(nchars):
                    key = word[:i]+'*'+word[i+1:]
                    if not(key in key_dict):
                        key_dict[key] = list([word])            
                    else:
                        key_dict[key].append(word)

            jobs = list( [(beginWord,0)] )

            visited = set({beginWord})
            while jobs:
                #dbg()
                cur_w,cur_i = jobs.pop(0)
                if cur_w == endWord:
                    return cur_i + 1
                else:
                    for i in range(nchars):
                        key = cur_w[:i]+'*'+cur_w[i+1:]
                        if key in key_dict:
                            next_words = key_dict[key]
                        else:
                            next_words = list()

                        for word in next_words:
                            if word in visited:
                                continue
                            else:
                                visited.add(word)                               
                                jobs.append( (word,cur_i+1) )
            
            return -1 + 1
        

if __name__ == "__main__":

    s = Solution()
    prt = lambda **kws: print(s.ladderLength(**kws))

    prt(beginWord = "dof",endWord = "cog",wordList = ["hot","dog","cog"]) # 2+1

    prt(beginWord = "tog",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]) # 1+1
    prt(beginWord = "dog",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]) # 1+1

    prt(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]) # 4+1
    prt(beginWord = "hot",endWord = "dog",wordList = ["hot","dot","dog","lot","log","cog"]) # 2+1

    prt(beginWord="qa", endWord= "sq", wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])

