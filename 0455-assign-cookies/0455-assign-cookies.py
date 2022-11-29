class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_pointer = 0
        s_pointer = 0
        while (s_pointer < len(s) and g_pointer < len(g)):
            if g[g_pointer] <= s[s_pointer]:
                g_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1
                
        return g_pointer