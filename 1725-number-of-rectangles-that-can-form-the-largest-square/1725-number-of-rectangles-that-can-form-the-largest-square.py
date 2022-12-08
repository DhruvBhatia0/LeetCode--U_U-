class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        res = 0
        for pair in rectangles:
            l = min(pair)
            if l > maxLen:
                maxLen = l
                res = 1
            elif l == maxLen: res += 1
        return res