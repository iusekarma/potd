class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return 1+y if (y:=time% (T:=2*n-2)) < n else T+1-y