class Solution:
    def isValid(self, s: str) -> bool:
        dic,stack = {')': '(', ']': '[', '}': '{'}, []
        for i in s:
            if stack and dic.get(i) == stack[-1]: stack.pop()
            else:                                 # we will tweak this else part only
                if i in dic: return False         # if i is in dic means we encountered closing and its opening was not there in top of stack, so its false
                stack.append(i)       
        return not stack