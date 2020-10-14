class Solution(object):
    def twoSum(nums,target):
        """
        :type nums: List[int]
        :type target: int
        :result: List[int]
        """
        # temporary result
        result = {}
        
        # looping with getting indexing
        for i,j in enumerate(nums):
            # get remaining data for get to know which indicies to target 
            remaining = target - j
            # save remaining data to list
            if remaining in result:
                return [result[remaining],i]
            
            result[j] = i
        
        return result
            
nums = [2,7,11,15]
target = 9 
           
pilot = Solution.twoSum(nums,target)

print(pilot)