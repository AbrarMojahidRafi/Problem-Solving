class Solution:
    def strStr(self, haystackStr, needleStr):
        try: 
            return haystackStr.index(needleStr)
        except:
            return -1

s = Solution()
print(s.strStr("sadbutsad", "sad"))