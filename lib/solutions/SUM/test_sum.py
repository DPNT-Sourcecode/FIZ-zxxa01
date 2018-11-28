import unittest
import sum_solution

class TestCompute(unittest.TestCase):
    def testSum(self):
	selfAssertEqual(compute(0,1),1)
	selfAssertEqual(compute(0,0),0)


