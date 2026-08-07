class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        left=0
        for write in range(1,len(nums)):
            if (nums[left]!=nums[write]):
                left+=1
                nums[left]=nums[write]
        return left+1

        