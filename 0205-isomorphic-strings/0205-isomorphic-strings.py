class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_comp = {}
        if (len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            if s[i] in letter_comp.keys():
                if letter_comp[s[i]] != t[i]:
                    return False
            else:
                if (t[i] in letter_comp.values()):
                    return False
                letter_comp[s[i]] = t[i]
        print(letter_comp)
        return True