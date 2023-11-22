class Solution:
    
    def addBinary(self, a_str, b_str):
        
        if len(a_str) > len(b_str):
            big = a_str
            small = b_str
        else:
            big = b_str
            small = a_str
        
        ans = ""
        carry = None 
        loopCounter = -1 
        while (loopCounter > -(len(small))-1):
            if small[loopCounter] == "0" and big[loopCounter] =="0":
                if carry == None or carry =="0": 
                    ans = "0" + ans 
                    carry = None
                else: 
                    if small[loopCounter] == "0" and big[loopCounter] =="0":
                        ans = "1" + ans
                        carry = None
                    elif (small[loopCounter] == "0" and big[loopCounter] =="1") or (small[loopCounter] == "1" and big[loopCounter] =="0"):
                        ans = "0" + ans 
                        carry = "1"
                    elif small[loopCounter] == "1" and big[loopCounter] =="1":
                        ans = "1" + ans 
                        carry = "1"
            elif (small[loopCounter] == "0" and big[loopCounter] =="1") or (small[loopCounter] == "1" and big[loopCounter] =="0"):
                if carry == None or carry =="0": 
                    ans = "1" + ans 
                    carry = None
                else: 
                    if small[loopCounter] == "0" and big[loopCounter] =="0":
                        ans = "1" + ans
                    elif (small[loopCounter] == "0" and big[loopCounter] =="1") or (small[loopCounter] == "1" and big[loopCounter] =="0"):
                        ans = "0" + ans 
                        carry = "1"
                    elif small[loopCounter] == "1" and big[loopCounter] =="1":
                        ans = "1" + ans 
                        carry = "1"
            elif small[loopCounter] == "1" and big[loopCounter] =="1":
                if carry == None or carry =="0": 
                    ans = "0" + ans
                    carry = "1"
                else: 
                    if small[loopCounter] == "0" and big[loopCounter] =="0":
                        ans = "1" + ans
                        carry = None 
                    elif (small[loopCounter] == "0" and big[loopCounter] =="1") or (small[loopCounter] == "1" and big[loopCounter] =="0"):
                        ans = "0" + ans 
                        carry = "1"
                    elif small[loopCounter] == "1" and big[loopCounter] =="1":
                        ans = "1" + ans 
                        carry = "1"
            loopCounter = loopCounter - 1 
        # print(loopCounter, big[:loopCounter+1])
        s = loopCounter 
        while (s > (-len(big)-1)):
            if carry == None or carry == "0": 
                ans = big[:s+1] + ans
                break
            else: 
                if big[s] == "1":
                    ans = "0" + ans
                    carry = "1"
                else: 
                    ans = "1" + ans 
                    carry = None 
            s = s - 1
            
        if carry != None:
            ans = carry + ans
        
        return ans
    
s = Solution()
print(s.addBinary("100", "110010"))