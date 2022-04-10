class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t = nums.count(val) #Counts how many times val occurs in the list
        
        for _ in range(t): #repeat as many times as val was found in the list
            nums.remove(val) #removes the first occurence of val
            
        return len(nums)