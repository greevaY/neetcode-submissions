class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # container water capacity = height * (difference between indices)
        # 1,7,2,5,4,7,3,6
        # 2 pointers beginning and end
        # if the capacity is higher than prev stored -> return it
        # to choose height, we'd choose the lower of the 2
        
        l = 0
        r = len(heights) -  1

        cap_m = 0
        
        while l < r:
            h = min(heights[l],heights[r])
            cap = h * (r-l)

            if cap > cap_m:
                cap_m = cap
            if h == heights[l]:
                l += 1
            else:
                r -= 1
                
        return cap_m                
