class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for letter in s:
            if letter in freq.keys():
                freq[letter] += 1
            else:
                freq[letter] = 1
        
        for letter in t:
            if letter in freq.keys():
                freq[letter] -= 1
            else:
                return False
        
        for key in freq.keys():
            if freq[key] != 0:
                return False
            
        return True