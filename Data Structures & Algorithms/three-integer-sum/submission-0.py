class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = len(nums)-1
            target = -nums[i]
            while L<R:
                sum = nums[L] + nums[R]
                if sum < target:
                    L +=1
                elif sum > target: 
                     R -=1
                else:
                     sum == target
                     result.append([nums[i], nums[L] , nums[R]])
                     L+=1
                     R-=1
                     while L<R and nums[L]==nums[L-1]:
                        L+=1
                     while L<R and nums[R]==nums[R+1]:
                        R-=1
        return result 