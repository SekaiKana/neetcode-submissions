class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        seen = []
        for right in range(len(s)):
            character = s[right]
            while character in seen:
                seen.remove(s[left])
                left = left + 1
            seen.append(character)
            
            result = max(result, right - left + 1)
        return result