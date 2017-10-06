import unittest

class unitest(unittest.TestCase):
    def testInvalidInput(self):
        Input = [0,0]
        ans = []
        self.assertEqual(Solution().threeSum(Input),ans);

class Solution():
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        return None

if __name__ == '__main__':
    unittest.main()
