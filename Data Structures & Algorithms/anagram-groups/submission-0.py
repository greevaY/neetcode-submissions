class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 2 pointers
        # both take an element 
        # compare the sorted version -> if same -> return them tgt

        d = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())
