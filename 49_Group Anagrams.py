import ipdb
dbg = ipdb.set_trace

def str_to_key(astr):
    return ('').join(sorted(astr))

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 1:
            return []

        anagrams = dict()
        for astr in strs:
            akey = str_to_key(astr)
            if akey in anagrams:
                anagrams[akey].append(astr)
            else:
                anagrams[akey] = [astr]

        return [lst for lst in anagrams.values()]

if __name__ == "__main__":
    s = Solution()
    dbg()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([]))
