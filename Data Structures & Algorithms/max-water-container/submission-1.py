class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        area = 0
        l = 0
        r = len(heights)-1
        while r > l:
            width = r-l
            height = min(heights[r], heights[l])
            area = width*height
            max_area = max(area, max_area)
            if r > l + 1 and heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max(max_area, area)