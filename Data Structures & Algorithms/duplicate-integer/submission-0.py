class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_map = dict()
        duplicate_indicator = False

        if len(nums) <= 1:
            return False

        for number in nums:
            if number in number_map.keys():
                number_map[number] += 1
                if number_map[number] > 1:
                    duplicate_indicator = True
            else:
                number_map[number] = 1
        
        return duplicate_indicator