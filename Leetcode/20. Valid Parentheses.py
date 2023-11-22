class Solution:
    def isValid(self, s):
        starting = "({["
        ending = ")}]"
        st = []
        for i in s: 
            if i in starting: 
                st.append(i)
            else: 
                if len(st) != 0: 
                    if (st[-1] == "(" and i ==")") or (st[-1] == "{" and i =="}") or (st[-1] == "[" and i =="]"):
                        if i == ")": 
                            st.pop()
                        elif i == "}": 
                            st.pop()
                        elif i == "]": 
                            st.pop()
                    else:
                        return False 
                else: 
                    return False

        if len(st) == 0: 
            return True 
        else: 
            return False 

s1 = Solution()
print(s1.isValid("()"))
print("================================")
print(s1.isValid("()[]{}"))
print("================================")
print(s1.isValid("(]"))
print("================================")
print(s1.isValid("([)]"))
print("================================")
print(s1.isValid("]"))
print("================================")
print(s1.isValid("[([]])"))