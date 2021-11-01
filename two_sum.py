class Solution:
    import typing
    def twoSum(self, nums:list, target:int):
        self.nums = nums
        self.target = target
        for a in nums:
            b = target - a
            target = a + b
            if (((b in nums) == True) and ((nums.index(a) != nums.index(b)))):
                return[nums.index(a),nums.index(b)]
            elif (a == b) and (a + b == target) and ((nums.index(a) != nums.index(b))):
                return[nums.index(a),nums.index(b)]
nums = [3,3]
target = 6
combo1 = Solution()
print(combo1.twoSum(nums,target))
