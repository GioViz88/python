class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        x = n // m
        inc = [0, 1, 2]
        for i in inc:
            if b in a * (x + i):
                return x + i
        return -1