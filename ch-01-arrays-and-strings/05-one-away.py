"""
#Determine whether the edit distance between two strings is less than 2.
"""

def func_oneawy(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1<l2:
        s1,s2=s2,s1
        l1,l2=l2,l1
    if l1-l2>1:
        return False
    cnt=0   
    if l1==l2:
         for i,j in zip(s1,s2):
             if i!=j:
                 cnt+=1   
         return True                 
    else:
        for i in xrange(len(s1)-1):
            if s1[i+cnt]!=s2[i] :
                cnt+=1
            if cnt>1:
                return False
        return True
                
        
        
from nose.tools import assert_equal

class test(object):
    
    def test(self,sol):
        assert_equal(sol('pale','ple'),True)
        assert_equal(sol('pales','pale'),True)
        assert_equal(sol('pale','bale'),True)
        assert_equal(sol('pale','bae'),False)



        print "ALL TEST CASES PASSED"

# Run Tests
t = test()
t.test(func_oneawy)
