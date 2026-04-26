class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                elif s < 0:
                    left = left + 1
                elif s > 0:
                    right = right - 1

        return result