class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":                            #extreme case
            return []
        mapping = { '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5' : ['j','k','l'], '6' : ['m','n','o'], '7' : ['p', 'q', 'r', 's'],  '8' :['t','u','v'], '9' : ['w','x','y','z'] }       #mapping of digits to letters
        q = deque()                                 
        i = 0                                       #first digit
        for letter in mapping[digits[i]]:
             q.append(letter)   
        for i in range(1,len(digits)):              #rest digits
            length = len(q)
            for j in range(length):                 #empty queue  
                subset  =  q.popleft()          
                for letter in mapping[digits[i]]:   #augment letters to subsets
                    q.append(subset+letter)         #put them back to the queue
        return q