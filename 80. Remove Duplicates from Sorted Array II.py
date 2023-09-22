from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq_dict = defaultdict(lambda: 0)
        for num in nums:
            freq_dict[num] += 1
        idx = 0
        while idx < len(nums):
            if freq_dict[nums[idx]] > 2:
                nums.pop(idx)
                freq_dict[nums[idx]] -= 1
            else:
                idx += 1

        return len(nums)