class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use two-pointer technique and handle duplicates
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Use two pointers for the remaining part of the array
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second position
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third position
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Sum is too small, move left pointer to increase sum
                    left += 1
                else:
                    # Sum is too large, move right pointer to decrease sum
                    right -= 1
        
        return result