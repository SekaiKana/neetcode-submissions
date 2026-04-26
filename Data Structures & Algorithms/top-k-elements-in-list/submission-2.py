class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            elif nums[i] in dic:
                dic[nums[i]] += 1

        sorted_dict = dict(sorted(dic.items(), key = lambda x: x[1], reverse=True))

        topk = list(sorted_dict.keys())[:k]
        return topk