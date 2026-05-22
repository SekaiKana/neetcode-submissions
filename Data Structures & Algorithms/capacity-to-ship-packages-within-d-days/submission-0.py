class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(m):
            ships, currCap = 1, m
            for w in weights:
                if currCap - w < 0:
                    ships = ships + 1
                    currCap = m
                currCap = currCap - w
            return ships <= days

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
            
        return res

