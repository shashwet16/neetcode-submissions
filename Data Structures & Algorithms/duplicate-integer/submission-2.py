class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         freq= {}
         for num in nums:
            freq[num] = freq.get(num ,0) +1
         
         for num in nums:
            if freq[num] > 1:
                return True
         return False # returned false outside the the for cuz when i was putting it inside , after #checking only one element it stopped the function causing the error 