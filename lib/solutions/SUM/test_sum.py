import unittest
import sum_solution

class TestCompute(unittest.TestCase):
    def testSum(self):
	self.assertEqual(sum_solution.compute(0,1),1)
	self.assertEqual(sum_solution.compute(0,0),0)




