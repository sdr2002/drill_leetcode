class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.stack = []
        
        for b in s:
            if len(self.stack < 1):
                self.stack.append(b)
            elif self.match(self.stack[-1],b):
                self.stack.pop()
            else:
                self.stack.append(b)
            
        if len(self.stack)!=0:
            return False
        else:
            return True
            
    
    def match(self,x,y):
        if (x=='(') and (y==')'):
            return True
        elif (x=='{') and (y=='}'):
            return True
        elif (x=='[') and (y==']'):
            return True
        else:
            return False
