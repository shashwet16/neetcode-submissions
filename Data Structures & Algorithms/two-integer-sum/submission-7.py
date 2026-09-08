class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {} # empty dict , value:indez 
       for i in range(len(nums)):
           current = nums[i]
           needed = target - current # main twosum formula 
           if needed in seen: 
             return [ seen[needed], i ]
           else :
             seen[current]=i 
            

               
            