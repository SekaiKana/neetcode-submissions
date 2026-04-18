class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        a = 0
        while left < right:
            width = right - left
            smaller = min(heights[left], heights[right])
            area = width * smaller
            if area > a:
                a = area
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        return a
            