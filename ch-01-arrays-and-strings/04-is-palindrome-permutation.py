"""
Determine whether or not a string is a permutation of a palindrome,
# ignoring spaces.
"""

def func_pp(s):
    s=s.strip().replace(" ", "")
    s=s.lower()
    dic=dict()
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    odd=0       
    for key in dic:
         if dic[key]%2!=0:
             odd+=1
         if odd>1:
             return False
    return True
  

from nose.tools import assert_equal

class test(object):
    
    def test(self,sol):
        assert_equal(sol('Tact Coa'),True)
        assert_equal(sol('deval modi'),False)

        print "ALL TEST CASES PASSED"

# Run Tests
t = test()
t.test(func_pp)
