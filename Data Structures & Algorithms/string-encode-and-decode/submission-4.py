
class Solution:

#a = ["hello", "world", "this", "is", "a", "test"]
#encode "5hello#5world#4this#2is#1a#4test#"
# 5#hello5#world4#this2#is1#a4#test


    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            l = len(i)
            s = s + f"{l}#{i}"
        return s


    def decode(self, s: str) -> List[str]:
        
        t = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j = j+1
            length = int(s[i:j])

            k = j + 1 + length
            a = s[j+1:k]

            t.append(a) 
            i = k

        return t


#string.split(separator, maxsplit)

