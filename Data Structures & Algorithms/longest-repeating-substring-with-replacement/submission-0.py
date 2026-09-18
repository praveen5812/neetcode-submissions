class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        max_length = 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1 
            maxFreq = max(hashmap.values())
            window_length = right - left + 1
            if window_length - maxFreq <= k:
                max_length = max(max_length, window_length)
            else:
                hashmap[s[left]] = hashmap[s[left]] - 1
                left = left + 1
        return  max_length

