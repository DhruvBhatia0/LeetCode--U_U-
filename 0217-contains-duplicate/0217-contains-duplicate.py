class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        the plan: take a number, map the difference of every element to that number. If we later see another element with the same difference, then return false
        '''
        difference = {}
        TARGET = 10
        for index, val in enumerate(nums):
            temp = TARGET - val
            if temp in difference.keys():
                return True
            difference[temp] = 0
        
        return False