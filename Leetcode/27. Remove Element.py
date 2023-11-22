class Solution:
    def removeElement(self, numsList, valInt):        
        k = 0
        indexForInPlace = 0
        for i in numsList:
            if i != valInt:
                k += 1
                numsList[indexForInPlace] = i
                indexForInPlace += 1
        print(numsList)
        return k

s = Solution()
print(s.removeElement([3,2,2,3], 3))