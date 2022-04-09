class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        min_current_sum = math.inf
        min_diff = math.inf
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            
            while l < r:            
                current_sum = nums[i] + nums[l] + nums[r]
                diff = abs(target-current_sum)
                if diff < min_diff:
                    min_current_sum = current_sum
                    min_diff = diff
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                elif current_sum == target:
                    return current_sum
                
        return min_current_sum