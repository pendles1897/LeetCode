from typing import List

class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        for a in nums:
            b = target - a
            if ((b in nums) == True and (nums.index(a) != nums.index(b))):
                return[nums.index(a),nums.index(b)]
nums = [2,4,6,8]
target = 12

combo1 = Solution()
print(combo1.twoSum(nums,target))
