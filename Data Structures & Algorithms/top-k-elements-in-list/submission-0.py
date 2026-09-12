class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        sorted_freq = sorted(freq.items() , key= lambda z :z[1] , reverse = True)
        result =[]
        for i in range(k):
            result.append(sorted_freq[i][0])
        return result 
        