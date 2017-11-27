import unittest

class unitest(unittest.TestCase):
    def testInvalidInput(self):
        Input = [0,0]
        ans = []
        self.assertEqual(Solution().threeSum(Input),ans);
    def testSampleInput(self):
        Input = [-1, 0, 1, 2, -1, -4]
        ans = [[-1, 0, 1],[-1, -1, 2]]
        self.assertEqual(Solution().threeSum(Input),ans);

class Solution():
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for z in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[z] == 0:
                        temp = [nums[i],nums[j],nums[z]]
                        ans.append(temp)
        newans = []
        for i in ans:
            if i not in newans:
                newans.append(i)
        return newans

if __name__ == '__main__':
    unittest.main()
