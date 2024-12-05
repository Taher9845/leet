class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        w_sum = 0
        n = len(nums)
        start = 0

        for i in range(n):
            w_sum += nums[i]

            if (i - start + 1) == k:
                avg = w_sum / k
                max_avg = max(avg, max_avg)
                w_sum -= nums[start]
                start += 1

        return max_avg