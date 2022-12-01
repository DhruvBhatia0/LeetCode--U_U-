class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        K = k
        if(K == 0):
            return num
        if(K == len(str(num))):
            return "0"
        l, stack = [int(x) for x in str(num)], []
        for i in l:
            while(K>0 and len(stack)>0 and stack[-1]>i):
                K -= 1
                stack.pop()
            stack.append(i)
        if K > 0:
            stack = stack[:-K]
        return str(int("".join([str(n) for n in stack])))