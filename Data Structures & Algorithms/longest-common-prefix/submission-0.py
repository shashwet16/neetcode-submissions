class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Prefix = strs[0]
        for word in strs[1:]: #strs[1:] means leave the first word and give all other words in strs 
            while not  word.startswith(Prefix):
               Prefix = Prefix[:-1] # if the word isnt same as the Prefix , shorten the Prefix by removing 1       element from the lasr (Prefix[:-1])
        return Prefix
          
        