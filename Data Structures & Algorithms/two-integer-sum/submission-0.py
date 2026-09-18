class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i, value in enumerate(nums):
             needed = target - value
             if needed in memory:
                return [memory[needed], i]
             else:
                memory[value] = i
