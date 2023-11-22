class Solution:
    def plusOne(self, digits_list_int):
        s = ""
        for i in digits_list_int:
            s = s + str(i)
        s = str(int(s) + 1) 
        
        l = []
        for i in s:
            l.append(int(i))
        
        return l
      

s = Solution()
print(s.plusOne([9]))