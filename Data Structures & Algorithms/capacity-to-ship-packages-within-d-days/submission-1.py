class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        res = right 

        def canShip(m):
            ships, currCap = 1, m
            for w in weights:
                if currCap - w < 0:
                    ships = ships + 1
                    currCap = m
                currCap = currCap - w
            return ships <= days

        while left <= right:
            m = (left + right) // 2
            if canShip(m):
                res = min(res, m)
                right = m - 1
            else:
                left = m + 1
            
        return res

