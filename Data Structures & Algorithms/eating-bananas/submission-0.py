class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        record = []
        
        while left <= right:
            mid = left + (right-left) // 2
            hours_needed = 0
            for pile in piles: 
                hours_needed += (pile + mid - 1) // mid

            if hours_needed <= h:
                result = mid
                right = mid - 1
            else: 
                left = mid + 1
            
        
        return result
        