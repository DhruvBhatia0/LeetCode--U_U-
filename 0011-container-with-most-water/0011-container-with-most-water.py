class Solution:
    def maxArea(self, height: List[int]) -> int:
        one_end = 0
        other_end = len(height) -1
        max = 0
        while (one_end <= other_end):
            vol = (other_end - one_end) * min(height[one_end], height[other_end])
            if (vol > max):
                max = vol
            if (height[one_end] > height[other_end]):
                other_end = other_end - 1
            else:
                one_end = one_end + 1
            
        return max
            