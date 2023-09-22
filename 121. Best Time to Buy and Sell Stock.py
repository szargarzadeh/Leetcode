class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        max_prof = 0
        for i in range(len(prices)):
            cur_min = min(prices[i], cur_min)
            max_prof = max(max_prof, prices[i] - cur_min)

        return max_prof