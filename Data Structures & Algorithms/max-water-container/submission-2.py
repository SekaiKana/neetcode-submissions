class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        total = 0
        while i < j:
            if heights[i] < heights[j]:
                val = heights[i] * (j - i)
                if val > total:
                    total = val
                i = i + 1
            elif heights[j] < heights[i]:
                val = heights[j] * (j - i)
                if val > total:
                    total = val
                j = j - 1
            elif heights[i] == heights[j]:
                val = heights[i] * (j - i)
                if val > total:
                    total = val
                i = i + 1
        return total
            