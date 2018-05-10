# Determine whether or not a given string contains no duplicate characters.

def check_dupl(s):
    return len(s)!=len(set(s))
def check_dupl1(s):
    s1=dict()
    for i in s:
        if i in s1:
            return True
        else:
            s1[i]=1
    return False
            
 

from nose.tools import assert_equal

class test(object):
    
    def test(self,sol):
        assert_equal(sol('abbc'),True)
        assert_equal(sol('abc'),False)
        print "ALL TEST CASES PASSED"

# Run Tests
t = test()
t.test(check_dupl)
t.test(check_dupl1)
