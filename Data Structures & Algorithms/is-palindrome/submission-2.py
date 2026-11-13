class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.replace(" ","")
        z = []
        for y in x:
            if y.isalnum() == True:
                z.append(y.lower())

        i = 0
        while i < (len(z)//2):
            a = len(z) - (i+1)
            if z[i] != z[a]:
                return False
            i = i + 1
        return True
