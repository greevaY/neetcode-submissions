class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        smallest = prices[0]
        dif = 0
    
        for price in prices: 
            if price < smallest: 
                smallest = price 
            
            if price - smallest > dif: 
                dif = price - smallest
        
        return dif 
            


        