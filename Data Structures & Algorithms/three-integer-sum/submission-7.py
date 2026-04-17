class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis = []
        nums.sort()
        i = 0
        while i < len(nums):
            
            if i > 0 and nums[i] == nums[i - 1]:
                i = i + 1
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res < 0:
                    j = j + 1
                elif res > 0:
                    k = k - 1
                elif res == 0:
                    lis.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i = i + 1
        return lis



        