class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
    
        ## Support Variabiles 
        len_str = len(haystack)
        len_needle = len(needle)

        ## Rolling Window of equality checking
        for sub in range(0, len_str-len(needle)+1):
            if haystack[sub:sub+len_needle] == needle:
                return sub

        ## If not found return -1
        return -1