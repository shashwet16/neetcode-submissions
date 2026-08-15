class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         freq1 = {}
         freq2= {}
         for str1 in s :
            freq1[str1] = freq1.get(str1 , 0)+1
         

         for str2  in t :
            freq2[str2] = freq2.get(str2, 0)+1
       
         return freq1 == freq2


            