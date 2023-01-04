from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if target - num in d.keys():
                return [d[target - num], index]
            else:
                d[num] = index


s = Solution()
answer = s.twoSum([9, 3, 2, 1, 5], 14)  # [0,4]
print(answer)
