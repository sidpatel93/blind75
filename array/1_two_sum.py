from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, a in enumerate(nums):
            # check if the hash map contains the another part of the sum with element a. If so return the indexes
            if target - a in hash_map:
                return [hash_map[target - a], i]
            # store the element and its index in the hash map if the other part of the sum is not found.
            hash_map[a] = i