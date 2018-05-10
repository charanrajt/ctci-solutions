"""
Add %20 at white space except at the end
"""

def urlify(s):
    return s.strip().replace(" ", "%20")
    
  

from nose.tools import assert_equal

class test(object):
    
    def test(self,sol):
        assert_equal(sol('charan raj  '),"charan%20raj")
        assert_equal(sol('deval modi'),"deval%20modi")

        print "ALL TEST CASES PASSED"

# Run Tests
t = test()
t.test(urlify)
