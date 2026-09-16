class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)# creating an array os the ssame lenght 
        prefiz = 1 # initally nothing is there beofre the fisrt element so we take as 1
        # first product calcualting the left product
        for i in range(len(nums)):
            answer[i] = prefiz # prefiz the the product of everything before for the i+1th elemnt   
            prefiz = prefiz*nums[i]
        #second pass - left rpdouct * right product
        suffiz = 1 # initally no elemnt after the last elemwnt 

        for i in range(len(nums)-1, -1 , -1): # range(start , stop , step )
                                            # range (3 , -1 , -1) - starts from 3 stops when -1 , increase by -1            
            answer[i] = answer[i]*suffiz # suffiz is everrthig after the ith elemnt 
                                        # we multiply because we have prefiz , we only need to multiply suffiz to get the real answer
            suffiz = suffiz*nums[i]

        return answer