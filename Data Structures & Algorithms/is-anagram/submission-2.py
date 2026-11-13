class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = 0
        x = []
        while i < len(s):
            x.append(s[i])
            i = i + 1
        j = 0
        y = []
        while j < len(t):
            y.append(t[j])
            j = j + 1
        
        x.sort()
        y.sort()
        
        if x == y:
            return True
        else:
            return False


