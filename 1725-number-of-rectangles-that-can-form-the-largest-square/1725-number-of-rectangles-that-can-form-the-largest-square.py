class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        counter = 0
        size = 0
        for i in rectangles:
            if (min(i[0],i[1]) > size):
                size = min(i[0],i[1])
                counter = 0
            elif (min(i[0],i[1]) == size):
                counter += 1
        return counter + 1