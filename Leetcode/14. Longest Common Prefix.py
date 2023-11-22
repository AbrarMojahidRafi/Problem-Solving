class Solution:
    def longestCommonPrefix(self, l):
        # finding the minimum length word 
        word = ""
        wordLen = float('inf')
        for i in l: 
            if len(i) < wordLen: 
                wordLen = len(i) 
                word = i 

        st = ""
        i = 0
        common = ""
        while i<len(word):
            first = None 
            second = None
            hold = l[0][i]
            for j in range(0, len(l)-1): 
                first = l[j][i]
                second = l[j+1][i]
                if first == second and first == hold: 
                    hold = second 
                else: 
                    hold = ""
                    break 
            st+=hold
            # print(i, st)
            common = ""
            for index in range(len(st)): 
                if index != 0:
                    if st[index] == l[-1][index] and st[index-1] == l[-1][index-1] == common[-1]: 
                        # if st[index] not in common: 
                            common += st[index]
                else: 
                    if st[index] == l[-1][index]: 
                        # if st[index] not in common: 
                            common += st[index] 
            # print(i, common)
            # temp += common
            i+=1

        return common
      
      
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))

