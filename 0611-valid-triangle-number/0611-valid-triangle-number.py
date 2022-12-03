class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #let the three sides be a,b,c
        '''a = random element, b = element larger than a, c = largest element of the three'''
        nums.sort()
        count = 0;
        b_pointer = 0
        c_pointer = 0
        for i in range(len(nums)-1, 1, -1):
            b_pointer = i - 1
            c_pointer = 0
            while (b_pointer != c_pointer):
                if (nums[b_pointer] + nums[c_pointer] > nums[i]):
                    #this is a valid triangle, and increasing c will also lead to valid triangles
                    count += b_pointer - c_pointer
                    b_pointer -= 1
                else:
                    c_pointer += 1
        
        return count
            
            
            