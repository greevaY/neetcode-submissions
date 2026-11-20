class Solution:
    def isPalindrome(self, s: str) -> bool:
        # join the split by removing space
        # check 1st pointer and last pointer if same return True
        # else return false

        s = "".join(c for c in s if c.isalnum()).lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True