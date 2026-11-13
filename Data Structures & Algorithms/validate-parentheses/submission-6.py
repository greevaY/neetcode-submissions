class Solution:
    def isValid(self, s: str) -> bool:

        n = len(s)

        x = []

        for i in range(n):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                x.append(s[i])
            else:
                if not x:
                    return False
                elif s[i] == ")":
                    if x.pop() == "(":
                        continue
                    else:
                        return False
                elif s[i] == "}":
                    if x.pop() == "{":
                        continue
                    else:
                        return False
                elif s[i] == "]":
                    if x.pop() == "[":
                        continue
                    else:
                        return False
            
        if not x:
            return True
        else:
            return False
                