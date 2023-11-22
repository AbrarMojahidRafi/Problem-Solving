class Solution:
    def lengthOfLastWord(self, s_str):
        space = 0
        for i in s_str:
            if i == " ":
                space += 1
            else:
                space = 0 
                
        length = 0
        starting = -1 - space 
        idx = starting
        while (idx >= (-len(s_str))):
            if s_str[idx] != " ":
                length += 1
            else: 
                break
            idx -= 1
            
        return length
      
      
s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))