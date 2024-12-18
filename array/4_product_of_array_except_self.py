# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
#     2 <= nums.length <= 105
#     -30 <= nums[i] <= 30
#     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in nums]
        # populate the prefixes in the output array.
        pre_fix = 1
        for i in range(len(nums)):
            output[i] = pre_fix
            # update the prefix
            pre_fix = pre_fix * nums[i]
        # populate the postfixe in the output array. loop from the last element
        post_fix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * post_fix
            # update the postfix
            post_fix = post_fix * nums[i]
        return output