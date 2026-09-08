class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Prefix = strs[0]
        for word in strs[1:]: #strs[1:] means leave the first word and give all other words in strs 
            while not  word.startswith(Prefix):
               Prefix = Prefix[:-1] # if the word isnt same as the Prefix , shorten the Prefix by removing 1       element from the lasr (Prefix[:-1])
        return Prefix
          
        prefiz = strs[0]
        for word in strs[1:]:# every word ezcept first the 1st one 
            while not word.startswith[prefiz]: #while loop because it runs until the cond is true if will stop at first iteration it 
            # if the word isnt same as prefiz remove the last element 

                prefiz =prefiz[:-1] # delete the last word of the string
        return prefiz
            
            