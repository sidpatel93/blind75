# Given an integer array nums, return the length of the longest strictly increasing
# subsequence

 

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1




from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialize the dp array
        dp = [1 for _ in nums]
        length = len(nums)
        # find the length of longest common subsequence ending at in index i
        for i in range(1,length):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
        result = 1
        for a in dp:
            result = max(result, a)
        return result