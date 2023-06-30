class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = right = 0
        seen = set()
        max_length = 0

        while right < n:
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                length = right - left + 1
                max_length = max(max_length, length)
                right += 1

        return max_length