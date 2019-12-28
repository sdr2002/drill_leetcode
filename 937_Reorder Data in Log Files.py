import ipdb
dbg = ipdb.set_trace
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let_list = []
        dig_list = []

        #dbg()        
        for st in logs:
            first_term = st.split(' ')[1]
            if first_term[0].isdigit():
                dig_list.append(st)
            else:
                let_list.append(st)
        
        #dbg()
        letid_list = []
        for w in let_list:
            wparsed = w.split(' ')
            letid_list.append((' ').join(wparsed[1:]+wparsed[0:1]))
        letid_list = sorted(letid_list)
        
        #dbg()
        sorted_let_list = []
        for wid in letid_list:
            widparsed = wid.split(' ')
            sorted_let_list.append((' ').join(widparsed[-1:]+widparsed[:-1]))
            
        return sorted_let_list + dig_list


if __name__ == "__main__":
    s = Solution()
    print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
