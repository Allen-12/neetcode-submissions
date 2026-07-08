class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()
        duplicate_indicator = False

        if len(nums) <= 1:
            return False

        for number in nums:
            if number in number_set:
                duplicate_indicator = True
            else:
                number_set.add(number)
        
        return duplicate_indicator