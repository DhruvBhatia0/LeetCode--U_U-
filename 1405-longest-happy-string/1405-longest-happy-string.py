class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = [] 
        remaining = Counter({'a':a,'b':b,'c':c,}) 
        (fence, _), (wedge, _) = remaining.most_common(2) 
        while remaining[fence] > 0 and remaining[wedge] > 0: 
            result.append(fence)
            remaining[fence] -= 1
            if len(result) >= 2 and result[-2] == fence:
                pass
            elif remaining[fence] > 0: 
                result.append(fence)
                remaining[fence] -= 1
        
            result.append(wedge)
            remaining[wedge] -= 1
            
            
            (fence, _), (wedge, _) = remaining.most_common(2)

        if remaining[fence] > 0:
            result.append(fence)
            remaining[fence] -= 1
            if remaining[fence] > 0:
                result.append(fence)

        return ''.join(result)