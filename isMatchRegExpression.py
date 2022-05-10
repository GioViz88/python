import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.search(f'^{p}$', s)
        