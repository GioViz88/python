class Solution:
    def ZigZagConvert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        i = 0
        p = 0
        length = len(s)
        slots = [""] * numRows
        down = True

        while i < length:
            slots[p] += s[i]
            if down and p == numRows - 1:
                down = False

            if not down and p == 0:
                down = True

            if down:
                p += 1
            else:
                p -= 1
            i += 1
        
                
        return ''.join(slots)