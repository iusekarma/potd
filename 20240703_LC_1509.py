class Solution:
    def minDifference(self, nums: List[int]) -> int:
        s = sorted(nums)
        if len(s) < 5:
            return 0
        out = s[-4] - s[0]
        for i in range(4):
            out = min(out, s[-(4-i)]-s[i])
        return out