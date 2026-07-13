class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise Exception("nums must have at least 2 integers")

        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))

        i = 0
        j = len(indexed_nums) - 1
        sum = 0

        while i < j:
            sum = indexed_nums[i][0] + indexed_nums[j][0]
            if sum == target:
                res = [indexed_nums[i][1], indexed_nums[j][1]]
                res.sort()
                return res
            elif sum > target:
                j -= 1
            else:
                i += 1