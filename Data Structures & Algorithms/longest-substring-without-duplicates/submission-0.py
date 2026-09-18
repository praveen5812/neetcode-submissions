class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = set()
        max_len = 0
        while right < len(s):
            curr = s[right]
            if s[right] not in window:
                window.add(s[right]) 
                max_len = max(max_len,right - left + 1)
                right += 1
            else:
                window.remove(s[left])
                left += 1
        
        return max_len      














#We use a window to represent a substring with unique characters.
#We expand the window by moving the right pointer.
#If the character is new, the window is valid and we update the maximum length.
#If a duplicate appears, we move the left pointer and remove characters until the duplicate is gone.
#We continue this process until the end of the string.
#The answer is the maximum valid window length seen at any time.