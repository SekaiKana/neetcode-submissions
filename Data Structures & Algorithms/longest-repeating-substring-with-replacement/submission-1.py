class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        for right in range(len(s)):
            character = s[right]
            if character not in count:
                count[s[right]] = 1
            elif character in count:
                count[s[right]] += 1
            m = max(count.values())
            if right - left + 1 - m <= k:
                max_len = right - left + 1
            else:
                count[s[left]] -= 1
                left = left + 1
        return max_len

