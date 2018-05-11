# Implement a stack with a function that returns the current minimum item.

class minstack(object):
    def __init__(self):
        self.arr=list()
    def push(self,val):
        if len(self.arr)==0:
            self.min=val
        self.arr.append(val-self.min)    
        if val<self.min:
            self.min=val        
        print self.arr
    def pop(self) :
        ans=self.arr.pop()
        if ans<0:
            v=self.min
            prev_min=v-ans
            self.min=prev_min
            return v
        else:
            return ans+self.min
    def top(self):
        ans=self.arr[-1]
        if ans<0:
            return self.min
        else:
            return ans+self.min        
    def getMin(self):
        return self.min
        
a=minstack()    
a.push(-2)
a.push(0)
a.push(-3)
print a.getMin()
print a.pop()
print a.top()
print a.getMin()

