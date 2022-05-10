class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # For storing answers in one set also will check if any value exists in nums
        checker = set()
        for i in range(len(nums)):
            # If value already in answer checker
            if nums[i] in checker:
                return [nums.index(target-nums[i]),i]
           
            else:
                checker.add(target-nums[i])