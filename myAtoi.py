class Solution:
    def myAtoi(self, s: str) -> int:
        n, t, flag = 0, 1, True
        # n represents the number we are trying to get
        #We set the flag to false at the start of '+', '-', or an integer
        for i in s:
            #This case will prevent having spaces in middle of the numbers
            #If flag is False, it will proceed to the exception handle and will return the last n value
            if i == ' ' and flag:
                continue            
            #This case will prevent having two signs or sign and spaces
            #If flag is False, it will proceed to the exception handle and will return the last n value
            elif i == '+' and flag:
                flag = False
                continue 
            #This case will prevent having two signs or sign and spaces. It will also set the negative sign
            #If flag is False, it will proceed to the exception handle and will return the last n value. 
            elif i== '-' and flag:
                flag = False
                t = -1
                continue
            #We will try to convert (i) to integer, if we can't we will return the last value    
            try:
                flag = False
                n = n*10 + int(i)
            except:
                    return min(max(n*t, -2147483648),2147483647)     
        return min(max(n*t, -2147483648),2147483647)