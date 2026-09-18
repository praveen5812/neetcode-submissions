class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}
        for ch in s:
            if ch in hashmap_s:
                hashmap_s[ch] = hashmap_s[ch] + 1
            else:
                hashmap_s[ch] = 1
        for ch in t:
            if ch in hashmap_t:
                hashmap_t[ch] = hashmap_t[ch] + 1
            else:
                hashmap_t[ch] = 1
        if hashmap_s == hashmap_t:
            return True
        else:
            return False