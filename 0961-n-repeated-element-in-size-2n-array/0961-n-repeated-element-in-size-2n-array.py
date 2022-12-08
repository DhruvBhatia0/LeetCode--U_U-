class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums = Counter(nums)
        return nums.most_common(1)[0][0]