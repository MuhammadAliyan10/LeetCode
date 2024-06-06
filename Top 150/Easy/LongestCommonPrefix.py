class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
      for i, char in enumerate(strs[0]):
         for value in strs[1:]:
            if i >= len(value) or char != value[i]:
               return strs[0][:i]
      return strs[0]

     
                
             


#! Time complexity is O(m . n)
#! Space complexity is O(1)
