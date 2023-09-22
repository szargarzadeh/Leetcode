class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, right = 0, 0
        cur_sum = nums[0]
        min_len = 10 ** 6
        while right < len(nums):
            if cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            else:
                right += 1
                if right < len(nums):
                    cur_sum += nums[right]

        if min_len < 10 ** 6:
            return min_len

        return 0

