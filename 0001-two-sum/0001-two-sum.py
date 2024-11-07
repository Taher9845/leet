class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in dictionary:
                return dictionary[complement], i
            dictionary[nums[i]] = i
            i+=1
        
        