from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            if len(s) == 0:
                return 0
            else:
                return 1
        p2 = 0
        arr = deque()
        max_len = 0
        while p2 < len(s):
            fast_char = s[p2]
            if fast_char not in arr:
                arr.append(fast_char)
                p2 += 1
                max_len = max(max_len, len(arr))
            else:
                arr.popleft()

        return max_len