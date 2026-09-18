class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_value = set()
        for value in  nums:
            if value in seen_value:
                return True
            else:
                seen_value.add(value)
        else:
            return False        