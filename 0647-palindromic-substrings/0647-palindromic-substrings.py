class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        #loop through every letter
        
        for i in range(len(s)):
            #two possiblilties, odd number of letter or even number of letter
            
            #check if this letter is the centre of an odd number of letters
            count += 1 #for single letter counter
            lhs = i-1
            rhs = i+2
            while lhs >= 0 and rhs < len(s)+1:
                if s[lhs:rhs] == s[lhs:rhs][::-1]:
                    count += 1
                    lhs -= 1
                    rhs += 1
                else:
                    break
                    
            #check if this letter is the centre of an even number of letters
            lhs = i
            rhs = i+2
            while lhs >= 0 and rhs < len(s)+1:
                if s[lhs:rhs] == s[lhs:rhs][::-1]:
                    count += 1
                    lhs -= 1
                    rhs += 1
                else:
                    break
            
            
            
        return count