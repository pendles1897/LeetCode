class Solution:
    from typing import List
    def numIdenticalPairs(self,nums: List[int]) -> int:
        count = 0
        size = len(nums)
        for i in range(size):
            for j in range(1,size):
                if nums[i] == nums[j] and i < j:
                    count+=1
        return count

test = Solution()
nums = [1,2,3,1,1,3]
print(test.numIdenticalPairs(nums))