class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0 
        right = rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2
            row = middle // cols
            col = middle % cols
            mid_value = matrix[row][col]
            if mid_value == target:
                return True
            elif mid_value <= target:
                left = middle + 1
            elif mid_value >= target:
                right = middle - 1
        return False