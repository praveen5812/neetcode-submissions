class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        runningproduct = 1
        for i in range(n):
            output[i] = runningproduct
            runningproduct *= nums[i]
        runningproduct = 1
        for i in range(n-1,-1,-1):
            output[i] *= runningproduct
            runningproduct *= nums[i]
        return output