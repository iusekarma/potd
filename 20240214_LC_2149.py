class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ret_arr = []
        i,j = 0,0
        while i < len(nums) or j < len(nums):
            if ((not ret_arr) or (ret_arr[-1] < 0)) and (i < len(nums)):
                if nums[i] >= 0:
                    ret_arr.append(nums[i])
                i+=1
            else:
                if j < len(nums):
                    if nums[j] < 0:
                        ret_arr.append(nums[j])
                    j+=1
        return ret_arr