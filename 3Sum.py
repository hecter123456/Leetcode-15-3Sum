import unittest

class unitest(unittest.TestCase):
    def testInvalidInput(self):
        Input = [0,0]
        ans = []
        self.assertEqual(Solution().threeSum(Input),ans);
    def testSampleInput(self):
        Input = [-1, 0, 1, 2, -1, -4]
        ans = [[-1, -1, 2],[-1, 0, 1]]
        self.assertEqual(Solution().threeSum(Input),ans);

class Solution():
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    if left < right and nums[left] == nums[left+1]:
                        left += 1
                    if left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans

if __name__ == '__main__':
    unittest.main()
