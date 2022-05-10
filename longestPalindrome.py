class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_count = 0
        max_str = ""
        for i in range(len(s)):
            l = r = i
            # odd case
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_count:
                    max_count = r - l + 1
                    max_str = s[l:r+1]
                l -= 1
                r += 1
                
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_count:
                    max_count = r - l + 1
                    max_str = s[l:r+1]
                l -= 1
                r += 1
            
        return max_str