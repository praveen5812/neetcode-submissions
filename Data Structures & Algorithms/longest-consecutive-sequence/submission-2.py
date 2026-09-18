class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in num_set:
            if n - 1 not in num_set:
                current_num = n
                length = 1
                while current_num + 1 in num_set:
                    current_num = current_num + 1
                    length += 1
               # if length > max_len:
                #    max_len = length
                max_len = max(max_len,length)
                #max(max_len,length)-we can use this instead of this if length > max_len:
                                                                            # max_len = length
        return max_len