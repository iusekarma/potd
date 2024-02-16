class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums)
        s, s_arr = 0, []
        for i in arr:
            s += i
            s_arr.append(s)
        for i in range(len(arr)-1,1,-1):
            if arr[i] < s_arr[i-1]:
                return s_arr[i]
        return -1