import ipdb
dbg = ipdb.set_trace

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_ind_hash = dict()
        self.val_list = list()
        self.size = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_ind_hash:
            return False
        else:
            self.val_ind_hash.update({val:self.size})
            self.val_list.append(val)
            self.size += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not(val in self.val_ind_hash) or (self.size < 1):
            return False
        else:
            ind_to_del = self.val_ind_hash[val]
            if ind_to_del != self.size-1:                
                self.val_list[ind_to_del] = self.val_list[self.size-1]
                self.val_ind_hash[self.val_list[self.size-1]] = ind_to_del
            self.val_ind_hash.pop(val)                
            self.val_list.pop(self.size-1)
            self.size -= 1
            return True        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.size < 1:
            return None
        else:
            return random.choice(self.val_list)

def main(sol,jobs,args):
    for job, arg in zip(jobs[1:],args[1:]):               
        print("Job: %s, Arg: %s"%(job,arg))
        dbg()
        if job == "insert":
            sol.insert(*arg)
        elif job == "remove":
            sol.remove(*arg)
        elif job == "getRandom":
            print(sol.getRandom())
        else:
            raise KeyError

        
        print(sol.__dict__)

if __name__ == "__main__":
    print("\n\n-----------Case1---------------")
    jobs = ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
    args = [[],[1],[2],[2],[],[1],[2],[]]
    #main(RandomizedSet(),jobs,args)

    print("\n\n-----------Case2---------------")
    jobs = ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
    args = [[],[0],[1],[0],[2],[1],[]]
    main(RandomizedSet(),jobs,args)

    

    
