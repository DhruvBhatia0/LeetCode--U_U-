class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        num = [i for i in num]
        num.sort()
        num1 = int(num[0] + num[2])
        num2 = int(num[1] + num[3])
        return num1 + num2