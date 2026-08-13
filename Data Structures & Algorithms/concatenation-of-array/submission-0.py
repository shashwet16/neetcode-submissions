class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            
             n = len(nums)
             ans = [0] * (2 * n)
             for i in range(0 , n):
                 ans[i] = nums[i] 
                 c = i + n 
                 ans[c] = nums[i]

             return ans