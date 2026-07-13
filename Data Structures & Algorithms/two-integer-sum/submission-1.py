class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {}   # value : index

        for index, value in enumerate(nums):
            difference = target - value
            if difference in previous_map:
                return [previous_map[difference], index]
            else:
                previous_map[value] = index
