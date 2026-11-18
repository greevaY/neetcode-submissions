class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {} 
    
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        dic = (sorted(dic.items(), key=lambda item: item[1]))

        dic = dic[::-1]
        
        result = []
        j = 0
        while j < k:
            result.append(dic[j][0])
            j = j + 1
        
        
        return result