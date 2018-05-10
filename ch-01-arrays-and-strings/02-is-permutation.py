"""
Determine whether or not a given string contains no duplicate characters.
"""

def check_perm(s1,s2):
    if len(s1)>len(s2):
        s1,s2=s2,s1
    temp=dict()   
    for i in s2:
        if i in temp:
            temp[i]=+1
        else:
            temp[i]=1
    for i in s1:
        if i in temp and temp[i]>0:
           temp[i]=-1
        else:
            return False
    return True     
            
 

from nose.tools import assert_equal

class test(object):
    
    def test(self,sol):
        assert_equal(sol('abbc','abc'),True)
        assert_equal(sol('abbc','ad'),False)

        print "ALL TEST CASES PASSED"

# Run Tests
t = test()
t.test(check_perm)
